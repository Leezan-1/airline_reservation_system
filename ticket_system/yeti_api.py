import requests
import json

params = {
  'api_key': '9a4a1aca-f6eb-441b-815c-df00a23239e5',
  'iata_code': 'YT',
  'icao_code': 'NYT',
  'country':'NP'
}
method = 'airlines'
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method, params)
api_response = api_result.json()

print(json.dumps(api_response, indent=4, sort_keys=True))