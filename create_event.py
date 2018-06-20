import requests
import json
import pprint
url = 'http://localhost:5000/api/v1/events'
for x in range(10000, 30001, 2000):
	data = {
	    "parameter":"CO",
	    "value": x
	}
	data_json = json.dumps(data)
	headers = {'Content-type': 'application/json'}
	response = requests.post(url, data=data_json, headers=headers)
	pprint.pprint(response.json())