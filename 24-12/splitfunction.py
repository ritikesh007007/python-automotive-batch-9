import re
s="hello"
i="e"
res=re.search(i,s)

if res:
    print("found")
else:
    print("not found")