def count(n):
    if n <=5:
        print("a")
    else:
        print(n)
        count(n-1)
    
count(5)
#recustion is when a function calls itesleft 