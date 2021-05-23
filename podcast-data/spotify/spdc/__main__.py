from spdc.helpers import TokenHelper as th
from spdc.helpers import DataHelper as dh

def get_show_id():
  with open('_sid.txt') as show_id_file:
      return show_id_file.read()

cookie_data, client_id = th.TokenHelper.get_local_tokens()
bearer_token_data = th.TokenHelper.get_bearer_token(cookie_data, client_id)

episode_data = dh.DataHelper.get_episode_data(show_id=get_show_id(),
  token=bearer_token_data['access_token'], start='2021-05-16', end='2021-05-22', page='1',
  size='50', sort_by='releaseDate', sort_order='descending', query_filter='')

print(episode_data)