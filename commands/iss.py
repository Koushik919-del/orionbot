import requests
import logging
from datetime import datetime, timezone

log = logging.getLogger(__name__)
ISS_API_URL = 'http://api.open-notify.org/iss-now.json'
CREW_API_URL = 'http://api.open-notify.org/astros.json'
GEOCODE_URL = 'https://nominatim.openstreetmap.org/reverse'

def handle_iss(respond):
    try:
        pos = _fetch_iss_position()
        loc = _reverse_geocode(pos['latitude'], pos['longitude'])
        crew = _fetch_crew_count()
        blocks = _build_iss_blocks(pos, loc, crew)
        respond(blocks=blocks, text=f'ISS is currently over {loc}')
    except Exception as e:
        log.error(f'ISS error: {e}')
        respond(text=f'Could not reach ISS telemetry. Error: {e}')

def _fetch_iss_position():
    resp = requests.get(ISS_API_URL, timeout=8)
    resp.raise_for_status()
    data = resp.json()
    pos = data['iss_position']
    return {'latitude': float(pos['latitude']), 'longitude': float(pos['longitude']), 'timestamp': int(data['timestamp'])}

def _reverse_geocode(lat, lon):
    try:
        params = {'lat': lat, 'lon': lon, 'format': 'json', 'zoom': 3}
        headers = {'User-Agent': 'OrionBot-HackClub/1.0'}
        resp = requests.get(GEOCODE_URL, params=params, headers=headers, timeout=6)
        resp.raise_for_status()
        address = resp.json().get('display_name', '')
        if address:
            return address.split(',')[-1].strip()
    except Exception:
        pass
    return 'open ocean or unknown territory'

def _fetch_crew_count():
    try:
        resp = requests.get(CREW_API_URL, timeout=6)
        resp.raise_for_status()
        people = [p for p in resp.json().get('people', []) if p.get('craft') == 'ISS']
        return len(people)
    except Exception:
        return -1

def _build_iss_blocks(pos, location, crew):
    lat = pos['latitude']
    lon = pos['longitude']
    ts = datetime.fromtimestamp(pos['timestamp'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    lat_label = f"{abs(lat):.4f} {'N' if lat >= 0 else 'S'}"
    lon_label = f"{abs(lon):.4f} {'E' if lon >= 0 else 'W'}"
    maps_url = f'https://www.google.com/maps?q={lat},{lon}&z=4'
    crew_text = f'{crew} astronauts aboard' if crew > 0 else 'crew count unavailable'
    return [
        {'type': 'header', 'text': {'type': 'plain_text', 'text': 'ISS Live Tracker', 'emoji': True}},
        {'type': 'section', 'text': {'type': 'mrkdwn', 'text': f'The ISS is flying over *{location}*\nCaptured at: {ts}'}},
        {'type': 'divider'},
        {'type': 'section', 'fields': [
            {'type': 'mrkdwn', 'text': f'*Latitude*\n{lat_label}'},
            {'type': 'mrkdwn', 'text': f'*Longitude*\n{lon_label}'},
            {'type': 'mrkdwn', 'text': f'*Crew*\n{crew_text}'},
            {'type': 'mrkdwn', 'text': '*Speed*\n~27,600 km/h'},
        ]},
        {'type': 'actions', 'elements': [{'type': 'button', 'text': {'type': 'plain_text', 'text': 'Open on Google Maps', 'emoji': True}, 'url': maps_url, 'action_id': 'iss_maps'}]},
        {'type': 'context', 'elements': [{'type': 'mrkdwn', 'text': 'Source: Open Notify ISS API - rerun for updated position'}]},
    ]
