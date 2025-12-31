import requests
import json

#uri= uniform resource identifier
#url= unifortm resource locator

#API endpoint URL
url="https://api.open-notify.org/astros.json"

#making the GET reqsuest=fetch the data
response=requests.get(url)

#the data i want to past as a python dictinary casue json and dictonary has same data strature 
post_data={
    "name":"Ritikesh",
    "age":22,
    "city":"Patna"
}

response=requests.post(url,data=post_data)