OrionBot

This is a Slack bot I built for Stardance. It connects your Slack workspace directly to NASA's live data feeds, so instead of opening a NASA site every time you want to check something, you just type a slash command and the data shows up right in your channel.

COMMANDS
/apod - pulls today's Astronomy Picture of the Day (sometimes it's a video instead of a photo)
/iss-track - shows where the ISS is right now
/mars - grabs the latest pictures of Mars from the Rover

SETUP
You'll need Python 3.10+, a Slack App with slash commands turned on, and a free NASA API key from api.nasa.gov (DEMO_KEY works fine if you're just testing). You'll also need a public HTTPS URL to point Slack at - ngrok is the easiest way to get one while developing locally.

Clone the repo, set up a virtual environment, and install the requirements. Copy .env.example to .env and fill in your Slack bot token, signing secret, and NASA API key. Then go set up your Slack App at api.slack.com/apps, add the commands scope and chat:write scope, and create the three slash commands pointing at your /slack/events endpoint.

Run app.py locally and use ngrok to expose it, then paste the ngrok URL into your Slack App's slash command settings. For real deployment I used gunicorn, and it ran fine on both Railway and Render without extra config.

DATA SOURCES
APOD comes from api.nasa.gov/planetary/apod, limited to 1,000 requests an hour on a free key.
ISS position and crew come from api.open-notify.org, which has no rate limit.
Mars Rover photos come from api.nasa.gov/mars-photos, also 1,000 requests an hour.
Reverse geocoding for the ISS map link uses Nominatim from OpenStreetMap, limited to 1 request a second.

NOTES
DEMO_KEY caps out at 30 requests an hour, so it's fine for messing around but you'll want a real key before putting this in front of people. ISS position updates every few seconds, so if you want a fresher location just run /mc-iss again.


For the Ship Reviewer: I'm sorry, I didn't know we can't use AI for the README

LICENSE
MIT - use it, break it, build on it.
