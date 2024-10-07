import requests
import json

r = requests.get("http://localhost:3000/students")

r_json = r.json()
print(r.status_code)
print(r_json[3]['name'])