import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"
data = {"name": "arpit", "roll": 45, "city": "Bhavnagar"}  # python data
json_data = json.dumps(data)  # converting python data to json

r = requests.post(url=URL, data=json_data)  # Print the response content
data = r.json()
print(data)
