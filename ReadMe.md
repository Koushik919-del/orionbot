# 🚀 OrionBot

OrionBot is a Slack bot I built for the Star Dance. It hooks your workspace into NASA's live data feeds, so instead of tabbing over to a NASA site, you just type a slash command and the data shows up in your channel.

---

## The Commands

Three slash commands, three live data pulls:

| Command | What you get |
|---|---|
| `/mc-apod` | Today's Astronomy Picture of the Day (sometimes it's a video) |
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

|
