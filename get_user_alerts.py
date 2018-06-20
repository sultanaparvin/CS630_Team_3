import requests
import json
import pprint
url = 'http://localhost:5000/api/v1/users/fmonsanto'
 
 
headers = {'Content-type': 'application/json'}
response = requests.get(url,  headers=headers)
pprint.pprint(response.json())