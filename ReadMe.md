# 🚀 OrionBot — NASA Deep Space Bridge for Slack

## What It Does

OrionBot adds three quick slash commands to pull **live cosmic data**:

| Command | What You Get |
|---|---|
| `/mc-apod` | Today's Astronomy Picture of the Day + breakdown |
| `/mc-iss` | Real-time ISS coordinates + map links |
| `/mc-mars` | Latest Mars temperature + Sol count from rover telemetry |

---

## Quick Start

### 1. Clone & Install
```bash
git clone [https://github.com/your-handle/orionbot](https://github.com/your-handle/orionbot)
cd orionbot
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt

#2. Configure The Environment
'cp .env.example .env'
