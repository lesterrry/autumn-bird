from sclib import SoundcloudAPI

def die(message):
	print(f'FATAL: {message}')
	exit(1)

api = SoundcloudAPI()
api.get_credentials()

client_id = api.client_id
if client_id is None or len(client_id) < 10:
	die('Client id is invalid')


