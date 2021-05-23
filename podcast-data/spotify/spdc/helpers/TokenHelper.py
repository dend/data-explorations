import json
import requests

class TokenHelper:
	def get_bearer_token(cookie_data, client_id):
	  url = f'https://generic.wg.spotify.com/creator-auth-proxy/v1/web/token?client_id={client_id}'

	  payload={}
	  headers = {
	    'Cookie': f'sp_dc={cookie_data["sp_dc"]};sp_key={cookie_data["sp_key"]}'
	  }

	  response = requests.request("GET", url, headers=headers, data=payload)

	  return json.loads(response.text)

	def get_local_tokens():
	  cookie_data = {}
	  client_id = ''

	  # Load JSON with cookie data
	  with open('_sc.json') as cookie_file:
	      cookie_data = json.load(cookie_file)

	  # Load client ID data
	  with open('_cid.txt') as client_id_file:
	      client_id = client_id_file.read()

	  return cookie_data, client_id