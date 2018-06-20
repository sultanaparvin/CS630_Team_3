import requests
import json
import pprint
url = 'http://localhost:5000/api/v1/rules/CO'
data = {
    "parameter":"CO",
    "threshold": 20000,
    "usernames":["fmonsanto"]
}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}
response = requests.put(url, data=data_json, headers=headers)
pprint.pprint(response.json())