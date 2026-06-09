# Cybersecurity Learning Discord Bot

Bot educativo de Discord para aprender ciberseguridad con comandos `!` y slash `/`.

## Funciones

- Quiz interactivo
- Modo práctica
- Modo challenge
- Flashcards
- Quiz por categoría
- Pregunta diaria
- Score personal
- Leaderboard
- Más de 60 preguntas

## Comandos

### Prefijo `!`
- `!quiz [amount] [category]`
- `!practice [amount] [category]`
- `!challenge [amount] [category]`
- `!flashcard [category]`
- `!category <name> [amount]`
- `!daily`
- `!score`
- `!leaderboard`
- `!categories`
- `!help`

### Slash `/`
- `/quiz`
- `/practice`
- `/challenge`
- `/flashcard`
- `/category`
- `/daily`
- `/score`
- `/leaderboard`
- `/categories`
- `/help`

## Categorías

- Network Security
- Web Security
- Cryptography
- Social Engineering
- Malware & Viruses
- Tools & Techniques
- Concepts & Fundamentals
- CTF & Hacking

## Requisitos

- Python 3.11 o superior
- Discord bot token
- Intent de `Message Content` activado en el portal de Discord si vas a usar comandos con `!`

## Instalación local

```bash
pip install -r requirements.txt
```

Crea una variable de entorno:

```bash
DISCORD_TOKEN=tu_token_aqui
```

Y ejecuta:

```bash
python main.py
```

## Deploy en Railway

1. Sube el proyecto a GitHub.
2. Crea un proyecto nuevo en Railway.
3. Conecta tu repositorio.
4. Añade la variable de entorno `DISCORD_TOKEN`.
5. Railway usará el `Procfile` y ejecutará:
   ```bash
   python main.py
   ```

## Notas

- El bot guarda estadísticas en `data/stats.json`.
- Si Railway reinicia el contenedor y no hay volumen persistente, esas estadísticas pueden reiniciarse.
- Para usar slash commands, el bot sincroniza automáticamente al iniciar.

## Estructura

- `main.py`
- `questions.py`
- `requirements.txt`
- `Procfile`
- `README.md`
