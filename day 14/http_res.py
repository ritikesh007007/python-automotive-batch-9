import requests

url="https://api.github.com"
response=requests.get(url)

print("Status Code:",response.status_code)
print("Headers:",response.headers)
for key, value in response.headers.items():
    print(f"{key}: {value}")
    
print("Response Body:")
print(response.text)