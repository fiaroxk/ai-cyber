# main.py
import os
import json
import random
from datetime import datetime, date
from pathlib import Path
from typing import Optional

import discord
from discord.ext import commands
from discord import app_commands

from questions import QUESTIONS, CATEGORIES, normalize_category

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"
DATA_DIR = Path("data")
STATS_FILE = DATA_DIR / "stats.json"

DATA_DIR.mkdir(exist_ok=True)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), intents=intents, help_command=None)

# ---------- Persistence ----------

def load_stats() -> dict:
    if STATS_FILE.exists():
        try:
            return json.loads(STATS_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def save_stats(stats: dict) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    STATS_FILE.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")

stats = load_stats()

def ensure_user(user_id: int) -> dict:
    sid = str(user_id)
    if sid not in stats:
        stats[sid] = {
            "correct": 0,
            "wrong": 0,
            "played": 0,
            "xp": 0,
            "last_daily": "",
        }
    return stats[sid]

def add_stats(user_id: int, correct: int = 0, wrong: int = 0, played: int = 0, xp: int = 0) -> None:
    entry = ensure_user(user_id)
    entry["correct"] += correct
    entry["wrong"] += wrong
    entry["played"] += played
    entry["xp"] += xp
    save_stats(stats)

# ---------- Helpers ----------

def clean_category_name(name: Optional[str]) -> Optional[str]:
    if not name:
        return None
    normalized = normalize_category(name)
    return normalized or None

def pick_questions(amount: int = 10, category: Optional[str] = None, difficulty: Optional[str] = None):
    pool = QUESTIONS
    if category:
        pool = [q for q in pool if q["category"] == category]
    if difficulty:
        pool = [q for q in pool if q["difficulty"] == difficulty]
    if not pool:
        return []
    amount = max(1, min(amount, len(pool)))
    return random.sample(pool, amount)

DIFFICULTY_ES = {"easy": "Fácil", "medium": "Medio", "hard": "Difícil"}

def question_embed(q: dict, index: int, total: int, title: str, reveal: bool = False, chosen: Optional[int] = None):
    embed = discord.Embed(
        title=f"{title} — {index}/{total}",
        description=q["question"],
        color=discord.Color.blurple(),
    )
    options = []
    letters = ["A", "B", "C", "D"]
    for i, option in enumerate(q["options"]):
        prefix = f"**{letters[i]}.** "
        if reveal and i == q["answer"]:
            options.append(f"{prefix}✅ {option}")
        elif reveal and chosen is not None and i == chosen and chosen != q["answer"]:
            options.append(f"{prefix}❌ {option}")
        else:
            options.append(f"{prefix}{option}")
    embed.add_field(name="Opciones", value="\n".join(options), inline=False)
    embed.add_field(name="Categoría", value=q["category"], inline=True)
    embed.add_field(name="Dificultad", value=DIFFICULTY_ES.get(q["difficulty"], q["difficulty"].title()), inline=True)
    if reveal:
        embed.add_field(name="Explicación", value=q["explanation"], inline=False)
    embed.set_footer(text="Responde con botones. Solo la persona que inició el reto puede contestar.")
    return embed

class AnswerView(discord.ui.View):
    def __init__(self, author_id: int, question: dict, timeout: int = 45):
        super().__init__(timeout=timeout)
        self.author_id = author_id
        self.question = question
        self.choice: Optional[int] = None
        self.correct: Optional[bool] = None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message("Solo la persona que inició el juego puede responder.", ephemeral=True)
            return False
        return True

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True

    async def _choose(self, interaction: discord.Interaction, idx: int):
        self.choice = idx
        self.correct = idx == self.question["answer"]
        for child in self.children:
            child.disabled = True
        embed = question_embed(
            self.question,
            1,
            1,
            "Resultado",
            reveal=True,
            chosen=idx,
        )
        if self.correct:
            embed.color = discord.Color.green()
            embed.description = "Correcto."
        else:
            embed.color = discord.Color.red()
            embed.description = "Incorrecto."
        await interaction.response.edit_message(embed=embed, view=self)
        self.stop()

    @discord.ui.button(label="A", style=discord.ButtonStyle.primary)
    async def a(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._choose(interaction, 0)

    @discord.ui.button(label="B", style=discord.ButtonStyle.primary)
    async def b(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._choose(interaction, 1)

    @discord.ui.button(label="C", style=discord.ButtonStyle.primary)
    async def c(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._choose(interaction, 2)

    @discord.ui.button(label="D", style=discord.ButtonStyle.primary)
    async def d(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self._choose(interaction, 3)

class FlashcardView(discord.ui.View):
    def __init__(self, author_id: int, question: dict, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.author_id = author_id
        self.question = question
        self.revealed = False

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message("Solo la persona que inició el estudio puede interactuar.", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="Mostrar respuesta", style=discord.ButtonStyle.success)
    async def reveal(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.revealed = True
        embed = discord.Embed(
            title="Flashcard",
            description=self.question["question"],
            color=discord.Color.gold(),
        )
        embed.add_field(name="Respuesta", value=f"**{self.question['options'][self.question['answer']]}**", inline=False)
        embed.add_field(name="Explicación", value=self.question["explanation"], inline=False)
        embed.add_field(name="Categoría", value=self.question["category"], inline=True)
        await interaction.response.edit_message(embed=embed, view=self)
        for child in self.children:
            child.disabled = True
        self.stop()

async def send_question(ctx: commands.Context, q: dict, index: int, total: int, title: str):
    view = AnswerView(ctx.author.id, q)
    embed = question_embed(q, index, total, title)
    msg = await ctx.send(embed=embed, view=view)
    await view.wait()
    if view.choice is None:
        try:
            await msg.edit(view=view)
        except Exception:
            pass
        return False
    return view.correct

async def run_quiz(ctx: commands.Context, questions: list[dict], title: str, practice: bool = False):
    correct = 0
    wrong = 0

    if ctx.interaction:
        try:
            await ctx.defer()
        except Exception:
            pass

    intro = discord.Embed(
        title=title,
        description=f"Preguntas: **{len(questions)}**\nModo: {'Práctica' if practice else 'Quiz'}",
        color=discord.Color.blurple(),
    )
    await ctx.send(embed=intro)

    for idx, q in enumerate(questions, start=1):
        view = AnswerView(ctx.author.id, q, timeout=60 if practice else 45)
        embed = question_embed(q, idx, len(questions), title)
        msg = await ctx.send(embed=embed, view=view)
        await view.wait()

        if view.choice is None:
            result = discord.Embed(
                title="Tiempo agotado",
                description=f"La respuesta correcta era: **{q['options'][q['answer']]}**",
                color=discord.Color.orange(),
            )
            result.add_field(name="Explicación", value=q["explanation"], inline=False)
            result.add_field(name="Categoría", value=q["category"], inline=True)
            result.add_field(name="Dificultad", value=DIFFICULTY_ES.get(q["difficulty"], q["difficulty"].title()), inline=True)
            await msg.edit(embed=result, view=None)
            wrong += 1
            continue

        if view.correct:
            correct += 1
        else:
            wrong += 1

        result = question_embed(q, idx, len(questions), title, reveal=True, chosen=view.choice)
        result.color = discord.Color.green() if view.correct else discord.Color.red()
        await msg.edit(embed=result, view=None)

        if practice:
            await ctx.send(f"**Explicación:** {q['explanation']}")

    add_stats(ctx.author.id, correct=correct, wrong=wrong, played=len(questions), xp=correct * (20 if practice else 25))
    summary = discord.Embed(
        title=f"Resultado de {title}",
        description=f"Correctas: **{correct}**\nIncorrectas: **{wrong}**\nPuntuación XP: **{correct * (20 if practice else 25)}**",
        color=discord.Color.green() if correct >= wrong else discord.Color.red(),
    )
    await ctx.send(embed=summary)

def current_daily_question() -> dict:
    today = date.today().isoformat()
    idx = int(hashlib.sha256(today.encode()).hexdigest(), 16) % len(QUESTIONS)
    return QUESTIONS[idx]

def build_rankboard(limit: int = 10):
    items = []
    for uid, data in stats.items():
        items.append((uid, data.get("xp", 0), data.get("correct", 0), data.get("played", 0)))
    items.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return items[:limit]

# ---------- Commands ----------

@bot.hybrid_command(name="quiz", description="Inicia un quiz de preguntas de ciberseguridad.")
@app_commands.describe(amount="Cantidad de preguntas (1-20)", category="Filtra por categoría")
async def quiz(ctx: commands.Context, amount: int = 10, category: Optional[str] = None):
    cat = clean_category_name(category)
    if category and not cat:
        await ctx.send(f"Categoría no válida. Usa una de estas: {', '.join(CATEGORIES)}")
        return
    questions = pick_questions(amount=amount, category=cat)
    if not questions:
        await ctx.send("No encontré preguntas para esa selección.")
        return
    await run_quiz(ctx, questions, title="Quiz")

@bot.hybrid_command(name="practice", description="Modo práctica con explicación después de cada respuesta.")
@app_commands.describe(amount="Cantidad de preguntas (1-20)", category="Filtra por categoría")
async def practice(ctx: commands.Context, amount: int = 5, category: Optional[str] = None):
    cat = clean_category_name(category)
    if category and not cat:
        await ctx.send(f"Categoría no válida. Usa una de estas: {', '.join(CATEGORIES)}")
        return
    questions = pick_questions(amount=amount, category=cat)
    if not questions:
        await ctx.send("No encontré preguntas para esa selección.")
        return
    await run_quiz(ctx, questions, title="Modo Práctica", practice=True)

@bot.hybrid_command(name="challenge", description="Modo desafío con preguntas aleatorias y tiempo más corto.")
@app_commands.describe(amount="Cantidad de preguntas (1-20)", category="Filtra por categoría")
async def challenge(ctx: commands.Context, amount: int = 5, category: Optional[str] = None):
    cat = clean_category_name(category)
    if category and not cat:
        await ctx.send(f"Categoría no válida. Usa una de estas: {', '.join(CATEGORIES)}")
        return
    pool = QUESTIONS
    if cat:
        pool = [q for q in pool if q["category"] == cat]
    hard_pool = [q for q in pool if q["difficulty"] in ("medium", "hard")]
    questions = random.sample(hard_pool or pool, k=min(amount, len(hard_pool or pool)))
    if not questions:
        await ctx.send("No encontré preguntas para esa selección.")
        return
    await run_quiz(ctx, questions, title="Modo Desafío", practice=False)

@bot.hybrid_command(name="flashcard", description="Modo flashcard para estudiar.")
@app_commands.describe(category="Filtra por categoría")
async def flashcard(ctx: commands.Context, category: Optional[str] = None):
    cat = clean_category_name(category)
    if category and not cat:
        await ctx.send(f"Categoría no válida. Usa una de estas: {', '.join(CATEGORIES)}")
        return
    pool = QUESTIONS if not cat else [q for q in QUESTIONS if q["category"] == cat]
    if not pool:
        await ctx.send("No encontré preguntas para esa selección.")
        return
    q = random.choice(pool)
    view = FlashcardView(ctx.author.id, q)
    embed = discord.Embed(
        title="Flashcard",
        description=q["question"],
        color=discord.Color.gold(),
    )
    embed.add_field(name="Categoría", value=q["category"], inline=True)
    embed.add_field(name="Dificultad", value=DIFFICULTY_ES.get(q["difficulty"], q["difficulty"].title()), inline=True)
    await ctx.send(embed=embed, view=view)

@bot.hybrid_command(name="category", description="Juega un quiz usando una categoría específica.")
@app_commands.describe(name="Nombre de la categoría", amount="Cantidad de preguntas (1-20)")
async def category(ctx: commands.Context, name: str, amount: int = 10):
    cat = clean_category_name(name)
    if not cat:
        await ctx.send(f"Categoría no válida. Usa una de estas: {', '.join(CATEGORIES)}")
        return
    questions = pick_questions(amount=amount, category=cat)
    if not questions:
        await ctx.send("No encontré preguntas para esa categoría.")
        return
    await run_quiz(ctx, questions, title=f"Quiz de Categoría: {cat}")

@bot.hybrid_command(name="daily", description="Resuelve la pregunta del día.")
async def daily(ctx: commands.Context):
    q = current_daily_question()
    entry = ensure_user(ctx.author.id)
    today = date.today().isoformat()
    if entry.get("last_daily") == today:
        await ctx.send("Ya resolviste la pregunta diaria de hoy. Vuelve mañana.")
        return
    view = AnswerView(ctx.author.id, q, timeout=60)
    embed = question_embed(q, 1, 1, "Reto Diario")
    msg = await ctx.send(embed=embed, view=view)
    await view.wait()
    if view.choice is None:
        await msg.edit(content="Se acabó el tiempo.", view=None)
        add_stats(ctx.author.id, wrong=1, played=1)
        return
    entry["last_daily"] = today
    save_stats(stats)
    if view.correct:
        add_stats(ctx.author.id, correct=1, played=1, xp=35)
        await msg.edit(content="¡Correcto! Ganaste XP extra por el daily.", view=None)
    else:
        add_stats(ctx.author.id, wrong=1, played=1)
        await msg.edit(content=f"Incorrecto. La respuesta era: **{q['options'][q['answer']]}**", view=None)

@bot.hybrid_command(name="score", description="Muestra tus estadísticas.")
async def score(ctx: commands.Context):
    entry = ensure_user(ctx.author.id)
    embed = discord.Embed(title=f"Score de {ctx.author.display_name}", color=discord.Color.blurple())
    embed.add_field(name="Correctas", value=str(entry["correct"]), inline=True)
    embed.add_field(name="Incorrectas", value=str(entry["wrong"]), inline=True)
    embed.add_field(name="Jugadas", value=str(entry["played"]), inline=True)
    embed.add_field(name="XP", value=str(entry["xp"]), inline=True)
    await ctx.send(embed=embed)

@bot.hybrid_command(name="leaderboard", description="Muestra el ranking por XP.")
async def leaderboard(ctx: commands.Context):
    board = build_rankboard()
    if not board:
        await ctx.send("Todavía no hay ranking.")
        return
    lines = []
    for i, (uid, xp, correct, played) in enumerate(board, start=1):
        user = bot.get_user(int(uid))
        name = user.name if user else f"Usuario {uid}"
        lines.append(f"**{i}. {name}** — XP: {xp} | ✔ {correct} | 🎯 {played}")
    embed = discord.Embed(title="Tabla de Clasificación", description="\n".join(lines), color=discord.Color.gold())
    await ctx.send(embed=embed)

@bot.hybrid_command(name="categories", description="Lista las categorías disponibles.")
async def categories(ctx: commands.Context):
    embed = discord.Embed(title="Categorías disponibles", description="\n".join(f"• {c}" for c in CATEGORIES), color=discord.Color.blurple())
    await ctx.send(embed=embed)

@bot.hybrid_command(name="help", description="Muestra ayuda del bot.")
async def help_cmd(ctx: commands.Context):
    text = (
        "**Comandos con prefijo:** `!quiz`, `!practice`, `!challenge`, `!flashcard`, `!category`, `!daily`, `!score`, `!leaderboard`, `!categories`, `!help`\n"
        "**Slash commands:** `/quiz`, `/practice`, `/challenge`, `/flashcard`, `/category`, `/daily`, `/score`, `/leaderboard`, `/categories`, `/help`\n\n"
        "Ejemplos:\n"
        "`!quiz 10`\n"
        "`/practice amount:5 category:Web Security`\n"
        "`/category name:Cryptography amount:8`"
    )
    await ctx.send(text)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print("Could not sync commands:", e)
    print(f"Logged in as {bot.user} ({bot.user.id})")

async def main():
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN no está configurado.")
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
