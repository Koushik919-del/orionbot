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
