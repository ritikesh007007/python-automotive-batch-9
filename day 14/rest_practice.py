import requests

url = "https://jsonplaceholder.typicode.com/users"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

if response.ok:
    for user in response.json():
        print(user)
