import requests
import json

def fetch_github():
    url = "https://api.github.com"
    
    response = requests.get(url)
    
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)  
    print("Response Data:")              
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    fetch_github()
