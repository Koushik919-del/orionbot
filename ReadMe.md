# 🚀 OrionBot

OrionBot is a Slack bot I built for the Star Dance. It hooks your workspace into NASA's live data feeds, so instead of tabbing over to a NASA site, you just type a slash command and the data shows up in your channel.

---

## The Commands 

Three slash commands, three live data pulls:

| Command | What you get |
|---|---|
| `/mc-apod` | Today's Astronomy Picture of the Day(Sometimes it might be a video)|
| `/mc-iss` | Where the ISS is right now |
| `/mc-mars` | Latest pictures of Mars from the Rover |

---

## Getting it running

### What you'll need
- Python 3.10+
- A [Slack App](https://api.slack.com/apps) with slash commands turned on
- A free [NASA API key](https://api.nasa.gov) (or `DEMO_KEY` if you just want to poke around)
- A public HTTPS URL — [ngrok](https://ngrok.com) is the easiest way to get one while developing locally

### 1. Grab the code

```bash
git clone https://github.com/your-handle/orionbot
cd orionbot
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set up your env file

```bash
cp .env.example .env
```

Then drop your credentials in:

```env
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
NASA_API_KEY=your_key_here
```

### 3. Set up the Slack App side

1. Head to [api.slack.com/apps](https://api.slack.com/apps) → **Create New App** → From Scratch
2. Under **OAuth & Permissions**, add these Bot Token Scopes:
   - `commands`
   - `chat:write`
3. Under **Slash Commands**, set up all three commands pointing at the same URL:

| Command | Request URL |
|---|---|
| `/apod` | `https://your-domain.com/slack/events` |
| `/iss-track` | `https://your-domain.com/slack/events` |
| `/mars-weather` | `https://your-domain.com/slack/events` |

4. Install the app to your workspace and grab the Bot Token.

### 4. Run it locally

```bash
# Terminal 1 — fire up the bot
python app.py

# Terminal 2 — expose it to the internet
ngrok http 3000
```

Take the ngrok HTTPS URL it spits out and paste it into the Request URL field for all three slash commands back in your Slack App settings.

### 5. Ship it for real

```bash
gunicorn --workers 2 --bind 0.0.0.0:$PORT "app:flask_app"
```

I've tested this on Railway and Render — both work without any extra config. Fly.io or a plain Linux VPS should be fine too.

---

## How it's organized

```
orionbot/
├── app.py                  # Flask + Slack Bolt — this is where commands get routed
├── commands/
│   ├── __init__.py
│   ├── apod.py             # /apod → NASA's APOD API
│   ├── iss.py               # /iss-track → Open Notify telemetry
│   └── mars.py              # /mars-weather → NASA InSight, falls back to MAAS2
├── requirements.txt
├── .env.example
└── README.md
```

---

## Where the data comes from

| Feature | API | Rate limit |
|---|---|---|
| APOD | `api.nasa.gov/planetary/apod` | 1,000 req/hr (free key) |
| ISS position | `api.open-notify.org/iss-now.json` | Unlimited |
| ISS crew | `api.open-notify.org/astros.json` | Unlimited |
| Mars weather | `api.nasa.gov/insight_weather/` | 1,000 req/hr |
| Mars weather fallback | `mars.nasa.gov` MAAS2 feed | Unlimited |
| Reverse geocoding | Nominatim (OpenStreetMap) | 1 req/sec |

---

