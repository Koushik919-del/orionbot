# 🚀 OrionBot — NASA Deep Space Bridge for Slack

> A Hack Club Slack bot that connects your channel directly to NASA's deep space databases.  
> Built for the NASA GitHub Hackathon · Star Dance

---

## What It Does

OrionBot adds three slash commands to your Slack workspace that pull **live data from NASA** on demand:

| Command | What It Returns |
|---|---|
| `/apod` | Today's Astronomy Picture of the Day + scientific breakdown |
| `/iss-track` | Real-time ISS latitude/longitude + map links |
| `/mars-weather` | Latest Mars surface temperature + Sol count from rover data |

---

## Setup Guide

### 1. Prerequisites

- Python 3.10+
- A [Slack App](https://api.slack.com/apps) with slash commands enabled
- A free [NASA API key](https://api.nasa.gov) (or use `DEMO_KEY` for testing)
- A public HTTPS endpoint (use [ngrok](https://ngrok.com) for local dev)

---

### 2. Clone & Install

```bash
git clone https://github.com/your-handle/orionbot
cd orionbot
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
NASA_API_KEY=your_key_here
```

---

### 4. Create Your Slack App

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → **Create New App** → From Scratch
2. Under **OAuth & Permissions**, add these Bot Token Scopes:
   - `commands`
   - `chat:write`
3. Under **Slash Commands**, create three commands:

| Command | Request URL |
|---|---|
| `/apod` | `https://your-domain.com/slack/events` |
| `/iss-track` | `https://your-domain.com/slack/events` |
| `/mars-weather` | `https://your-domain.com/slack/events` |

4. **Install the app** to your workspace and copy the Bot Token.

---

### 5. Run Locally with ngrok

```bash
# Terminal 1 — start the bot
python app.py

# Terminal 2 — expose it to the internet
ngrok http 3000
```

Copy the ngrok HTTPS URL (e.g. `https://abc123.ngrok.io`) and paste it as the Request URL for all three slash commands in the Slack App settings.

---

### 6. Production Deployment

```bash
# Using gunicorn (recommended)
gunicorn --workers 2 --bind 0.0.0.0:$PORT "app:flask_app"
```

Works great on **Railway**, **Render**, **Fly.io**, or any Linux VPS.

---

## Project Structure

```
orionbot/
├── app.py                  # Flask + Slack Bolt listener, command routing
├── commands/
│   ├── __init__.py
│   ├── apod.py             # /apod handler → NASA APOD API
│   ├── iss.py              # /iss-track handler → Open Notify telemetry
│   └── mars.py             # /mars-weather → NASA InSight / MAAS2
├── requirements.txt
├── .env.example
└── README.md
```

---

## Data Sources

| Feature | API | Rate Limit |
|---|---|---|
| APOD | `api.nasa.gov/planetary/apod` | 1,000 req/hr (free key) |
| ISS Position | `api.open-notify.org/iss-now.json` | Unlimited |
| ISS Crew | `api.open-notify.org/astros.json` | Unlimited |
| Mars Weather | `api.nasa.gov/insight_weather/` | 1,000 req/hr |
| Mars Fallback | `mars.nasa.gov` MAAS2 feed | Unlimited |
| Reverse Geocode | Nominatim (OpenStreetMap) | 1 req/sec |

---

## Notes

- **InSight lander** officially ended operations Dec 2022 — the API still serves archived sols. The bot automatically falls back to Curiosity rover data (MAAS2) if InSight is unavailable.
- **DEMO_KEY** works for quick testing but is limited to 30 req/hr. Get a free key at [api.nasa.gov](https://api.nasa.gov) for production.
- ISS position updates every ~5 seconds; rerun `/iss-track` for a fresh fix.

---

## License

MIT — hack freely 🚀
