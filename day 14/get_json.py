import json
a={"name":"Ritikesh","age":22}

#key <> value 
#json -->javascript object notation
#test.docx
#data.json
b= json.dumps(a)

#{"age":22}

with open ("data.json","w") as f:
    data=json.load(f)
print(json.dumps(data, indent=4))