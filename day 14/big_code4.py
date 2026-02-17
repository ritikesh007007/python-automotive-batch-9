import requests

try:
    response = requests.get("https://wrongurl.test", timeout=3)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error:", e)
