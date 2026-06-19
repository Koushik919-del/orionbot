import os
import requests
import logging

log = logging.getLogger(__name__)
NASA_APOD_URL = 'https://api.nasa.gov/planetary/apod'

def handle_apod(respond):
    try:
        data = _fetch_apod()
        blocks = _build_apod_blocks(data)
        respond(blocks=blocks, text=f"APOD: {data.get('title', 'Todays Space Image')}")
    except Exception as e:
        log.error(f'APOD error: {e}')
        respond(text=f'Could not fetch APOD. Error: {e}')

def _fetch_apod():
    params = {'api_key': os.environ.get('NASA_API_KEY', 'DEMO_KEY'), 'thumbs': 'true'}
    resp = requests.get(NASA_APOD_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def _build_apod_blocks(data):
    title = data.get('title', 'Unknown')
    date = data.get('date', 'Unknown date')
    explanation = data.get('explanation', 'No description available.')
    media_type = data.get('media_type', 'image')
    url = data.get('url', '')
    hdurl = data.get('hdurl', url)
    copyright_ = data.get('copyright', '').strip()
    if len(explanation) > 2800:
        explanation = explanation[:2800] + '...'
    blocks = [
        {'type': 'header', 'text': {'type': 'plain_text', 'text': 'Astronomy Picture of the Day', 'emoji': True}},
        {'type': 'section', 'text': {'type': 'mrkdwn', 'text': f'*{title}*\n{date}' + (f' | Copyright {copyright_}' if copyright_ else '')}},
    ]
    if media_type == 'image':
        blocks.append({'type': 'image', 'image_url': url, 'alt_text': title})
    elif media_type == 'video':
        thumb = data.get('thumbnail_url', '')
        if thumb:
            blocks.append({'type': 'image', 'image_url': thumb, 'alt_text': title})
        blocks.append({'type': 'section', 'text': {'type': 'mrkdwn', 'text': f'<{url}|Watch the video>'}})
    blocks.append({'type': 'divider'})
    blocks.append({'type': 'section', 'text': {'type': 'mrkdwn', 'text': f'*Scientific Breakdown*\n{explanation}'}})
    if hdurl and media_type == 'image':
        blocks.append({'type': 'actions', 'elements': [{'type': 'button', 'text': {'type': 'plain_text', 'text': 'View Full Resolution', 'emoji': True}, 'url': hdurl, 'action_id': 'apod_hd_link'}]})
    blocks.append({'type': 'context', 'elements': [{'type': 'mrkdwn', 'text': 'Source: NASA Astronomy Picture of the Day API'}]})
    return blocks
