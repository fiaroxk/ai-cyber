# main.py — Bot de Discord de Ciberseguridad (todo en español)
import os
import json
import random
import hashlib
from datetime import date
from pathlib import Path
from typing import Optional

import discord
from discord.ext import commands
from discord import app_commands

from preguntas import (
    PREGUNTAS, CATEGORIAS, DIFICULTAD_COLOR,
    normalizar_categoria, normalizar_dificultad,
)

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIJO = "!"
DIR_DATOS = Path("datos")
ARCHIVO_STATS = DIR_DATOS / "stats.json"
DIR_DATOS.mkdir(exist_ok=True)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(PREFIJO),
    intents=intents,
    help_command=None,
)

# ──────────────────────────────────────────────
# Persistencia
# ──────────────────────────────────────────────

def cargar_stats() -> dict:
    if ARCHIVO_STATS.exists():
        try:
            return json.loads(ARCHIVO_STATS.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def guardar_stats(stats: dict) -> None:
    DIR_DATOS.mkdir(exist_ok=True)
    ARCHIVO_STATS.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")

stats = cargar_stats()

def asegurar_usuario(uid: int) -> dict:
    sid = str(uid)
    if sid not in stats:
        stats[sid] = {"correctas": 0, "incorrectas": 0, "jugadas": 0, "xp": 0, "ultimo_diario": ""}
    return stats[sid]

def agregar_stats(uid: int, correctas=0, incorrectas=0, jugadas=0, xp=0):
    e = asegurar_usuario(uid)
    e["correctas"] += correctas
    e["incorrectas"] += incorrectas
    e["jugadas"] += jugadas
    e["xp"] += xp
    guardar_stats(stats)

# ──────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────

DIFICULTAD_LABEL = {"fácil": "Fácil 🟢", "medio": "Medio 🟡", "difícil": "Difícil 🔴"}

def seleccionar_preguntas(
    cantidad: int = 10,
    categoria: Optional[str] = None,
    dificultad: Optional[str] = None,
) -> list[dict]:
    pool = PREGUNTAS
    if categoria:
        pool = [p for p in pool if p["categoria"] == categoria]
    if dificultad:
        pool = [p for p in pool if p["dificultad"] == dificultad]
    if not pool:
        return []
    cantidad = max(1, min(cantidad, len(pool)))
    return random.sample(pool, cantidad)

def embed_pregunta(
    p: dict,
    indice: int,
    total: int,
    titulo: str,
    revelar: bool = False,
    elegida: Optional[int] = None,
) -> discord.Embed:
    embed = discord.Embed(
        title=f"{titulo} — {indice}/{total}",
        description=f"**{p['pregunta']}**",
        color=discord.Color.blurple(),
    )
    letras = ["A", "B", "C", "D"]
    lineas = []
    for i, opcion in enumerate(p["opciones"]):
        prefijo = f"**{letras[i]}.** "
        if revelar and i == p["respuesta"]:
            lineas.append(f"{prefijo}✅ {opcion}")
        elif revelar and elegida is not None and i == elegida and elegida != p["respuesta"]:
            lineas.append(f"{prefijo}❌ {opcion}")
        else:
            lineas.append(f"{prefijo}{opcion}")
    embed.add_field(name="Opciones", value="\n".join(lineas), inline=False)
    embed.add_field(name="Categoría", value=p["categoria"], inline=True)
    embed.add_field(name="Dificultad", value=DIFICULTAD_LABEL.get(p["dificultad"], p["dificultad"].title()), inline=True)
    if revelar:
        embed.add_field(name="💡 Explicación", value=p["explicacion"], inline=False)
    embed.set_footer(text="Responde con los botones. Solo quien inició el reto puede contestar.")
    return embed

# ──────────────────────────────────────────────
# Vistas (botones)
# ──────────────────────────────────────────────

class VistaRespuesta(discord.ui.View):
    def __init__(self, autor_id: int, pregunta: dict, timeout: int = 45):
        super().__init__(timeout=timeout)
        self.autor_id = autor_id
        self.pregunta = pregunta
        self.eleccion: Optional[int] = None
        self.correcto: Optional[bool] = None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.autor_id:
            await interaction.response.send_message(
                "⛔ Solo la persona que inició el juego puede responder.", ephemeral=True
            )
            return False
        return True

    async def on_timeout(self):
        for hijo in self.children:
            hijo.disabled = True

    async def _elegir(self, interaction: discord.Interaction, idx: int):
        self.eleccion = idx
        self.correcto = idx == self.pregunta["respuesta"]
        for hijo in self.children:
            hijo.disabled = True
        embed = embed_pregunta(self.pregunta, 1, 1, "Resultado", revelar=True, elegida=idx)
        embed.color = discord.Color.green() if self.correcto else discord.Color.red()
        embed.description = "✅ **¡Correcto!**" if self.correcto else "❌ **Incorrecto.**"
        await interaction.response.edit_message(embed=embed, view=self)
        self.stop()

    @discord.ui.button(label="A", style=discord.ButtonStyle.primary)
    async def boton_a(self, interaction: discord.Interaction, _: discord.ui.Button):
        await self._elegir(interaction, 0)

    @discord.ui.button(label="B", style=discord.ButtonStyle.primary)
    async def boton_b(self, interaction: discord.Interaction, _: discord.ui.Button):
        await self._elegir(interaction, 1)

    @discord.ui.button(label="C", style=discord.ButtonStyle.primary)
    async def boton_c(self, interaction: discord.Interaction, _: discord.ui.Button):
        await self._elegir(interaction, 2)

    @discord.ui.button(label="D", style=discord.ButtonStyle.primary)
    async def boton_d(self, interaction: discord.Interaction, _: discord.ui.Button):
        await self._elegir(interaction, 3)


class VistaFlashcard(discord.ui.View):
    def __init__(self, autor_id: int, pregunta: dict, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.autor_id = autor_id
        self.pregunta = pregunta

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.autor_id:
            await interaction.response.send_message(
                "⛔ Solo quien inició el estudio puede interactuar.", ephemeral=True
            )
            return False
        return True

    @discord.ui.button(label="Mostrar respuesta", style=discord.ButtonStyle.success)
    async def revelar(self, interaction: discord.Interaction, boton: discord.ui.Button):
        p = self.pregunta
        embed = discord.Embed(title="🃏 Flashcard", description=f"**{p['pregunta']}**", color=discord.Color.gold())
        embed.add_field(name="✅ Respuesta", value=f"**{p['opciones'][p['respuesta']]}**", inline=False)
        embed.add_field(name="💡 Explicación", value=p["explicacion"], inline=False)
        embed.add_field(name="Categoría", value=p["categoria"], inline=True)
        embed.add_field(name="Dificultad", value=DIFICULTAD_LABEL.get(p["dificultad"], p["dificultad"]), inline=True)
        boton.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)
        self.stop()

# ──────────────────────────────────────────────
# Lógica de quiz
# ──────────────────────────────────────────────

async def ejecutar_quiz(
    ctx: commands.Context,
    preguntas: list[dict],
    titulo: str,
    practica: bool = False,
):
    correctas = 0
    incorrectas = 0

    if ctx.interaction:
        try:
            await ctx.defer()
        except Exception:
            pass

    intro = discord.Embed(
        title=titulo,
        description=f"Preguntas: **{len(preguntas)}**\nModo: {'🎓 Práctica' if practica else '⚡ Quiz'}",
        color=discord.Color.blurple(),
    )
    await ctx.send(embed=intro)

    for idx, p in enumerate(preguntas, start=1):
        timeout = 60 if practica else 45
        vista = VistaRespuesta(ctx.author.id, p, timeout=timeout)
        embed = embed_pregunta(p, idx, len(preguntas), titulo)
        msg = await ctx.send(embed=embed, view=vista)
        await vista.wait()

        if vista.eleccion is None:
            resultado = discord.Embed(
                title="⏰ Tiempo agotado",
                description=f"La respuesta correcta era: **{p['opciones'][p['respuesta']]}**",
                color=discord.Color.orange(),
            )
            resultado.add_field(name="💡 Explicación", value=p["explicacion"], inline=False)
            resultado.add_field(name="Categoría", value=p["categoria"], inline=True)
            resultado.add_field(name="Dificultad", value=DIFICULTAD_LABEL.get(p["dificultad"], p["dificultad"]), inline=True)
            await msg.edit(embed=resultado, view=None)
            incorrectas += 1
            continue

        if vista.correcto:
            correctas += 1
        else:
            incorrectas += 1

        resultado = embed_pregunta(p, idx, len(preguntas), titulo, revelar=True, elegida=vista.eleccion)
        resultado.color = discord.Color.green() if vista.correcto else discord.Color.red()
        await msg.edit(embed=resultado, view=None)

        if practica:
            await ctx.send(f"💡 **Explicación:** {p['explicacion']}")

    xp_ganado = correctas * (20 if practica else 25)
    agregar_stats(ctx.author.id, correctas=correctas, incorrectas=incorrectas, jugadas=len(preguntas), xp=xp_ganado)

    color_final = discord.Color.green() if correctas >= incorrectas else discord.Color.red()
    resumen = discord.Embed(
        title=f"📊 Resultado de {titulo}",
        description=(
            f"✅ Correctas: **{correctas}**\n"
            f"❌ Incorrectas: **{incorrectas}**\n"
            f"⭐ XP ganado: **{xp_ganado}**"
        ),
        color=color_final,
    )
    await ctx.send(embed=resumen)

def pregunta_diaria() -> dict:
    hoy = date.today().isoformat()
    idx = int(hashlib.sha256(hoy.encode()).hexdigest(), 16) % len(PREGUNTAS)
    return PREGUNTAS[idx]

def construir_ranking(limite: int = 10):
    items = [
        (uid, d.get("xp", 0), d.get("correctas", 0), d.get("jugadas", 0))
        for uid, d in stats.items()
    ]
    items.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return items[:limite]

# ──────────────────────────────────────────────
# Comandos
# ──────────────────────────────────────────────

@bot.hybrid_command(name="quiz", description="Inicia un quiz de ciberseguridad.")
@app_commands.describe(cantidad="Número de preguntas (1-20)", categoria="Filtra por categoría", dificultad="fácil / medio / difícil")
async def cmd_quiz(ctx: commands.Context, cantidad: int = 10, categoria: Optional[str] = None, dificultad: Optional[str] = None):
    cat = normalizar_categoria(categoria) if categoria else None
    dif = normalizar_dificultad(dificultad) if dificultad else None
    if categoria and not cat:
        await ctx.send(f"❌ Categoría no válida. Usa: {', '.join(CATEGORIAS)}")
        return
    if dificultad and not dif:
        await ctx.send("❌ Dificultad no válida. Usa: fácil, medio, difícil")
        return
    preguntas = seleccionar_preguntas(cantidad=cantidad, categoria=cat, dificultad=dif)
    if not preguntas:
        await ctx.send("❌ No encontré preguntas para esa selección.")
        return
    await ejecutar_quiz(ctx, preguntas, titulo="⚡ Quiz")


@bot.hybrid_command(name="practica", description="Modo práctica: muestra explicación tras cada respuesta.")
@app_commands.describe(cantidad="Número de preguntas (1-20)", categoria="Filtra por categoría", dificultad="fácil / medio / difícil")
async def cmd_practica(ctx: commands.Context, cantidad: int = 5, categoria: Optional[str] = None, dificultad: Optional[str] = None):
    cat = normalizar_categoria(categoria) if categoria else None
    dif = normalizar_dificultad(dificultad) if dificultad else None
    if categoria and not cat:
        await ctx.send(f"❌ Categoría no válida. Usa: {', '.join(CATEGORIAS)}")
        return
    if dificultad and not dif:
        await ctx.send("❌ Dificultad no válida. Usa: fácil, medio, difícil")
        return
    preguntas = seleccionar_preguntas(cantidad=cantidad, categoria=cat, dificultad=dif)
    if not preguntas:
        await ctx.send("❌ No encontré preguntas para esa selección.")
        return
    await ejecutar_quiz(ctx, preguntas, titulo="🎓 Modo Práctica", practica=True)


@bot.hybrid_command(name="desafio", description="Modo desafío: preguntas de dificultad media y alta con tiempo reducido.")
@app_commands.describe(cantidad="Número de preguntas (1-20)", categoria="Filtra por categoría")
async def cmd_desafio(ctx: commands.Context, cantidad: int = 5, categoria: Optional[str] = None):
    cat = normalizar_categoria(categoria) if categoria else None
    if categoria and not cat:
        await ctx.send(f"❌ Categoría no válida. Usa: {', '.join(CATEGORIAS)}")
        return
    pool = PREGUNTAS if not cat else [p for p in PREGUNTAS if p["categoria"] == cat]
    pool_dificil = [p for p in pool if p["dificultad"] in ("medio", "difícil")]
    pool_final = pool_dificil or pool
    preguntas = random.sample(pool_final, k=min(cantidad, len(pool_final)))
    if not preguntas:
        await ctx.send("❌ No encontré preguntas para esa selección.")
        return
    await ejecutar_quiz(ctx, preguntas, titulo="🔥 Modo Desafío", practica=False)


@bot.hybrid_command(name="flashcard", description="Muestra una flashcard para estudiar un concepto.")
@app_commands.describe(categoria="Filtra por categoría")
async def cmd_flashcard(ctx: commands.Context, categoria: Optional[str] = None):
    cat = normalizar_categoria(categoria) if categoria else None
    if categoria and not cat:
        await ctx.send(f"❌ Categoría no válida. Usa: {', '.join(CATEGORIAS)}")
        return
    pool = PREGUNTAS if not cat else [p for p in PREGUNTAS if p["categoria"] == cat]
    if not pool:
        await ctx.send("❌ No encontré preguntas para esa selección.")
        return
    p = random.choice(pool)
    vista = VistaFlashcard(ctx.author.id, p)
    embed = discord.Embed(title="🃏 Flashcard", description=f"**{p['pregunta']}**", color=discord.Color.gold())
    embed.add_field(name="Categoría", value=p["categoria"], inline=True)
    embed.add_field(name="Dificultad", value=DIFICULTAD_LABEL.get(p["dificultad"], p["dificultad"]), inline=True)
    await ctx.send(embed=embed, view=vista)


@bot.hybrid_command(name="categoria", description="Juega un quiz de una categoría específica.")
@app_commands.describe(nombre="Nombre de la categoría", cantidad="Número de preguntas (1-20)")
async def cmd_categoria(ctx: commands.Context, nombre: str, cantidad: int = 10):
    cat = normalizar_categoria(nombre)
    if not cat:
        await ctx.send(f"❌ Categoría no válida. Usa: {', '.join(CATEGORIAS)}")
        return
    preguntas = seleccionar_preguntas(cantidad=cantidad, categoria=cat)
    if not preguntas:
        await ctx.send("❌ No encontré preguntas para esa categoría.")
        return
    await ejecutar_quiz(ctx, preguntas, titulo=f"📂 Quiz: {cat}")


@bot.hybrid_command(name="diario", description="Responde la pregunta del día y gana XP extra.")
async def cmd_diario(ctx: commands.Context):
    p = pregunta_diaria()
    entrada = asegurar_usuario(ctx.author.id)
    hoy = date.today().isoformat()
    if entrada.get("ultimo_diario") == hoy:
        await ctx.send("📅 Ya completaste el reto diario de hoy. ¡Vuelve mañana!")
        return
    vista = VistaRespuesta(ctx.author.id, p, timeout=60)
    embed = embed_pregunta(p, 1, 1, "📅 Reto Diario")
    msg = await ctx.send(embed=embed, view=vista)
    await vista.wait()
    if vista.eleccion is None:
        await msg.edit(content="⏰ Se acabó el tiempo para el reto diario.", view=None)
        agregar_stats(ctx.author.id, incorrectas=1, jugadas=1)
        return
    entrada["ultimo_diario"] = hoy
    guardar_stats(stats)
    if vista.correcto:
        agregar_stats(ctx.author.id, correctas=1, jugadas=1, xp=35)
        await msg.edit(content="✅ ¡Correcto! Ganaste **35 XP** extra por el reto diario.", view=None)
    else:
        agregar_stats(ctx.author.id, incorrectas=1, jugadas=1)
        await msg.edit(
            content=f"❌ Incorrecto. La respuesta era: **{p['opciones'][p['respuesta']]}**",
            view=None,
        )


@bot.hybrid_command(name="puntuacion", description="Muestra tus estadísticas.")
async def cmd_puntuacion(ctx: commands.Context):
    entrada = asegurar_usuario(ctx.author.id)
    jugadas = entrada["jugadas"]
    correctas = entrada["correctas"]
    tasa = f"{(correctas / jugadas * 100):.1f}%" if jugadas > 0 else "—"
    embed = discord.Embed(
        title=f"📊 Estadísticas de {ctx.author.display_name}",
        color=discord.Color.blurple(),
    )
    embed.add_field(name="✅ Correctas", value=str(correctas), inline=True)
    embed.add_field(name="❌ Incorrectas", value=str(entrada["incorrectas"]), inline=True)
    embed.add_field(name="🎯 Jugadas", value=str(jugadas), inline=True)
    embed.add_field(name="⭐ XP Total", value=str(entrada["xp"]), inline=True)
    embed.add_field(name="📈 Tasa de acierto", value=tasa, inline=True)
    await ctx.send(embed=embed)


@bot.hybrid_command(name="ranking", description="Muestra el ranking de los mejores jugadores.")
async def cmd_ranking(ctx: commands.Context):
    tabla = construir_ranking()
    if not tabla:
        await ctx.send("📋 Todavía no hay jugadores en el ranking.")
        return
    medallas = ["🥇", "🥈", "🥉"]
    lineas = []
    for i, (uid, xp, correctas, jugadas) in enumerate(tabla, start=1):
        usuario = bot.get_user(int(uid))
        nombre = usuario.name if usuario else f"Usuario {uid}"
        icono = medallas[i - 1] if i <= 3 else f"**{i}.**"
        lineas.append(f"{icono} **{nombre}** — ⭐ {xp} XP | ✅ {correctas} | 🎯 {jugadas}")
    embed = discord.Embed(
        title="🏆 Tabla de Clasificación",
        description="\n".join(lineas),
        color=discord.Color.gold(),
    )
    await ctx.send(embed=embed)


@bot.hybrid_command(name="categorias", description="Lista todas las categorías disponibles.")
async def cmd_categorias(ctx: commands.Context):
    embed = discord.Embed(
        title="📚 Categorías disponibles",
        description="\n".join(f"• {c}" for c in CATEGORIAS),
        color=discord.Color.blurple(),
    )
    await ctx.send(embed=embed)


@bot.hybrid_command(name="ayuda", description="Muestra la ayuda del bot.")
async def cmd_ayuda(ctx: commands.Context):
    texto = (
        "**🤖 Bot de Ciberseguridad — Comandos disponibles**\n\n"
        "**Quiz y juegos:**\n"
        "`/quiz [cantidad] [categoria] [dificultad]` — Quiz estándar\n"
        "`/practica [cantidad] [categoria] [dificultad]` — Práctica con explicaciones\n"
        "`/desafio [cantidad] [categoria]` — Preguntas difíciles con tiempo reducido\n"
        "`/flashcard [categoria]` — Flashcard para estudiar\n"
        "`/categoria <nombre> [cantidad]` — Quiz de una categoría específica\n"
        "`/diario` — Pregunta del día (+35 XP)\n\n"
        "**Estadísticas:**\n"
        "`/puntuacion` — Tus estadísticas personales\n"
        "`/ranking` — Tabla de clasificación global\n\n"
        "**Info:**\n"
        "`/categorias` — Ver todas las categorías\n"
        "`/ayuda` — Este mensaje\n\n"
        "**Ejemplos:**\n"
        "`/quiz cantidad:10 dificultad:difícil`\n"
        "`/practica categoria:Criptografía`\n"
        "`!desafio 5 redes`"
    )
    await ctx.send(texto)


# ──────────────────────────────────────────────
# Eventos
# ──────────────────────────────────────────────

@bot.event
async def on_ready():
    try:
        sincronizados = await bot.tree.sync()
        print(f"✅ {len(sincronizados)} slash commands sincronizados.")
    except Exception as e:
        print("⚠️  No se pudieron sincronizar los comandos:", e)
    print(f"🤖 Bot conectado como {bot.user} ({bot.user.id})")


async def main():
    if not TOKEN:
        raise RuntimeError("❌ La variable de entorno DISCORD_TOKEN no está configurada.")
    async with bot:
        await bot.start(TOKEN)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
