import requests

session = requests.Session()

response1 = session.get("https://jsonplaceholder.typicode.com/users")
response2 = session.get("https://jsonplaceholder.typicode.com/users")

print("First Call Status:", response1.status_code)
print("Second Call Status:", response2.status_code)
