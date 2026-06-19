import os
import requests
import logging

log = logging.getLogger(__name__)
MAAS2_URL = 'https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json'

def handle_mars(respond):
    try:
        data, source = _fetch_mars_weather()
        blocks = _build_mars_blocks(data, source)
        respond(blocks=blocks, text=f"Mars Weather - Sol {data.get('sol', '?')}")
    except Exception as e:
        log.error(f'Mars error: {e}')
        respond(text=f'Mars weather feed unavailable right now. Error: {e}')

def _fetch_mars_weather():
    resp = requests.get(MAAS2_URL, timeout=10)
    resp.raise_for_status()
    reports = resp.json().get('soles', [])
    if not reports:
        raise ValueError('No weather data returned')
    latest = reports[0]
    return {
        'sol': latest.get('sol'),
        'min_temp': _safe_float(latest.get('min_temp')),
        'max_temp': _safe_float(latest.get('max_temp')),
        'season': latest.get('season', 'Unknown'),
        'earth_date': latest.get('terrestrial_date', ''),
    }, 'NASA Curiosity Rover'

def _safe_float(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return None

def _fmt_temp(val, unit='C'):
    if val is None:
        return 'N/A'
    return f'{val:.1f} {unit}'

def _build_mars_blocks(data, source):
    sol = data.get('sol', '?')
    min_c = data.get('min_temp')
    max_c = data.get('max_temp')
    season = data.get('season', 'Unknown')
    earth_date = data.get('earth_date', 'Unknown')
    def to_f(c):
        return None if c is None else c * 9/5 + 32
    return [
        {'type': 'header', 'text': {'type': 'plain_text', 'text': 'Mars Surface Weather', 'emoji': True}},
        {'type': 'section', 'text': {'type': 'mrkdwn', 'text': f'*Sol {sol}* - Martian Day {sol}\nEarth date: {earth_date}  |  Season: {season.title()}'}},
        {'type': 'divider'},
        {'type': 'section', 'fields': [
            {'type': 'mrkdwn', 'text': f'*High Temp*\n{_fmt_temp(max_c)} ({_fmt_temp(to_f(max_c), "F")})'},
            {'type': 'mrkdwn', 'text': f'*Low Temp*\n{_fmt_temp(min_c)} ({_fmt_temp(to_f(min_c), "F")})'},
            {'type': 'mrkdwn', 'text': '*Air Density*\n~1% of Earth'},
            {'type': 'mrkdwn', 'text': '*Sol Length*\n24 hrs 37 min'},
        ]},
        {'type': 'context', 'elements': [{'type': 'mrkdwn', 'text': f'Source: {source}'}]},
    ]
