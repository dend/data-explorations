import json
import requests

class DataHelper:
	def get_episode_data(show_id, token, start, end, page, size, sort_by, sort_order, query_filter):
		url = f'https://generic.wg.spotify.com/podcasters/v0/shows/{show_id}/episodes?end={end}&filter={query_filter}&page={page}&size={size}&sortBy={sort_by}&sortOrder={sort_order}&start={start}'

		payload={}
		headers = {
			'Authorization': f'Bearer {token}'
		}

		response = requests.request("GET", url, headers=headers, data=payload)

		return json.loads(response.text)