```markdown
# 🚀 OrionBot — NASA Deep Space Bridge for Slack

> A Hack Club Slack bot connecting your channel straight to NASA's deep space databases. 
> Built for the NASA GitHub Hackathon · Star Dance

---

## What It Does

OrionBot adds three quick slash commands to pull **live cosmic data**:

| Command | What You Get |
|---|---|
| `/apod` | Today's Astronomy Picture of the Day + breakdown |
| `/iss-track` | Real-time ISS coordinates + map links |
| `/mars-weather` | Latest Mars temperature + Sol count from rover telemetry |

---

## Quick Start

### 1. Clone & Install
```bash
git clone [https://github.com/your-handle/orionbot](https://github.com/your-handle/orionbot)
cd orionbot
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt

```

### 2. Configure Environment

```bash
cp .env.example .env

```

Pop open `.env` and add your tokens:

```env
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
NASA_API_KEY=your_key_here  # Or use DEMO_KEY

```

### 3. Setup Slack App

1. Create a new app at [api.slack.com/apps](https://api.slack.com/apps) (From Scratch).
2. Under **OAuth & Permissions**, add bot scopes: `commands` and `chat:write`.
3. Create the three slash commands (`/apod`, `/iss-track`, `/mars-weather`) pointing to your request URL: `https://your-domain.com/slack/events`.
4. Install to your workspace and grab the bot token.

### 4. Run Locally

```bash
# Terminal 1 — Start the bot
python app.py

# Terminal 2 — Expose it
ngrok http 3000

```

Copy your ngrok HTTPS URL and drop it into your Slack slash command settings.

---

## Deployment

For production, run it with gunicorn:

```bash
gunicorn --workers 2 --bind 0.0.0.0:$PORT "app:flask_app"

```

Deploys instantly to **Railway**, **Render**, **Fly.io**, or any standard VPS.

---

## Project Structure

```
orionbot/
├── app.py                  # Main Flask + Slack Bolt listener
├── commands/
│   ├── apod.py             # /apod handler → NASA APOD API
│   ├── iss.py              # /iss-track handler → Open Notify
│   └── mars.py             # /mars-weather → NASA InSight / MAAS2
├── requirements.txt
└── README.md

```

---

## Good to Know

* **Mars Fallback:** Since the InSight lander retired, the bot automatically switches to live Curiosity rover data (MAAS2) if needed.
* **Rate Limits:** `DEMO_KEY` caps at 30 req/hr. Grab a free production key at [api.nasa.gov](https://api.nasa.gov) for 1,000 req/hr.

---

## License

MIT — hack freely 🚀

```

```
