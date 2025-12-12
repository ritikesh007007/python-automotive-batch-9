def is_prime(n):
    if n <= 1:
        return false
    if n<=3:
        return true
    if n%2==0 or n%3==0:
        return false
    
    #check form 5 to sqrt(n)
    i=5
    while i*2<=n:
        if n%i==0 or n%(i+2)==0:
            return false
        i+=6
    return true
