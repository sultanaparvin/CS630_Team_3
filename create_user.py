import requests
import json
import pprint
url = 'http://localhost:5000/api/v1/users'

data = {"username" : "fmonsanto"}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)
pprint.pprint(response.json())

data = {"username" : "rvitorino"}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)
pprint.pprint(response.json())