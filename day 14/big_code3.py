#using header and timeout
import requests

url = "https://httpbin.org/get"

headers = {
    "User-Agent": "MyPythonApp",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, timeout=5)

print(response.status_code)
print(response.json())

