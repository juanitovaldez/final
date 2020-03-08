import requests
import json
import pandas as pd
from pandas.io.json import json_normalize

base_url = r'https://statsapi.web.nhl.com/api/v1/'
section = r'game/'
game_id = r'2019020921/'
options = r'feed/live'
req_url = f'{base_url}{section}{game_id}{options}'

r = requests.get(req_url)
r= r.json()