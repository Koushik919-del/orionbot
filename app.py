import os
import logging
from flask import Flask, request
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

# Enable logging
logging.basicConfig(level=logging.INFO)

# Initialize Slack Bolt App
app = App(
    token="xoxb-2210535565-11393247973702-pQynW3aq5sZjcRlnfq7GlKpx",
    signing_secret="99a358f606d3f51a5e18e37bd0b2d679"
)
handler = SlackRequestHandler(app)

# Initialize Flask for local routing
flask_app = Flask(__name__)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# Reach inside the commands folder to grab your logic modules
from commands.apod import handle_apod
from commands.iss import handle_iss
from commands.mars import handle_mars

@app.command("/apod")
def listen_apod(ack, respond):
    ack()
    handle_apod(respond)

@app.command("/iss-track")
def listen_iss(ack, respond):
    ack()
    handle_iss(respond)

@app.command("/mars")
def listen_mars(ack, respond):
    ack()
    handle_mars(respond)

if __name__ == "__main__":
    # Render automatically assigns a PORT variable; locally we fall back to 3000
    port = int(os.environ.get("PORT", 3000))
    print(f"🚀 OrionBot lifting off on port {port}")
    flask_app.run(host="0.0.0.0", port=port)
