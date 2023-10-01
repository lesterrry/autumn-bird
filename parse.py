from sclib import SoundcloudAPI
import json

JSON_FILE = '/Users/lesterrry/Downloads/freq.json'

def die(message):
	print(f'FATAL: {message}')
	exit(1)

api = SoundcloudAPI()
api.get_credentials()

client_id = api.client_id
if client_id is None or len(client_id) < 10:
	die('Client id is invalid')

print(f'Fetched: {client_id}')

with open(JSON_FILE, 'r+', encoding='utf-8') as f:
	existing = json.load(f)
	existing['sc_key'] = client_id
	f.seek(0)
	json.dump(existing, f, indent=2, ensure_ascii=False)
	f.truncate()

print('File written')

