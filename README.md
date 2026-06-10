# 🤖 Bot de Ciberseguridad para Discord

Bot educativo de ciberseguridad completamente en español. Incluye quizzes, modo práctica, desafíos, flashcards y sistema de XP.

## 📋 Requisitos

- Python 3.11+
- Un token de bot de Discord

## 🚀 Despliegue en Railway

1. Sube estos archivos a tu repositorio de GitHub.
2. En Railway, crea un nuevo proyecto → **Deploy from GitHub repo**.
3. En **Variables de entorno**, añade:
   ```
   DISCORD_TOKEN = tu_token_aquí
   ```
4. Railway detectará el `Procfile` automáticamente y desplegará el bot.

## ⚙️ Instalación local

```bash
pip install -r requirements.txt
export DISCORD_TOKEN="tu_token_aquí"
python main.py
```

## 🎮 Comandos

| Comando | Descripción |
|---|---|
| `/quiz` | Quiz estándar de ciberseguridad |
| `/practica` | Modo práctica con explicaciones |
| `/desafio` | Preguntas difíciles, tiempo reducido |
| `/flashcard` | Flashcard para estudiar |
| `/categoria <nombre>` | Quiz de categoría específica |
| `/diario` | Pregunta del día (+35 XP) |
| `/puntuacion` | Tus estadísticas |
| `/ranking` | Tabla de clasificación global |
| `/categorias` | Lista de categorías |
| `/ayuda` | Ayuda del bot |

Todos los comandos también funcionan con el prefijo `!` (ej: `!quiz 10`).

## 📚 Categorías

- Seguridad de Redes
- Seguridad Web
- Criptografía
- Ingeniería Social
- Malware y Virus
- Herramientas y Técnicas
- Conceptos y Fundamentos
- CTF y Hacking Ético

## ⭐ Sistema de XP

| Modo | XP por respuesta correcta |
|---|---|
| Quiz / Desafío | 25 XP |
| Práctica | 20 XP |
| Reto Diario | 35 XP |
