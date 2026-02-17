def count(n):
    c=1
    while c<=n:
        yield c
        c+=1
    
for value in count(4):
    print(value)
    
#generater asre memory effisicent thats why it is used 
