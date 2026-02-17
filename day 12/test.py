#use the decorater calulater for addition of two number by using the decorater @calculater 
def calculater(func):
    def inner(a,b,c):
        return func(a,b,c)
    
    return inner
@calculater
def add(a,b,c):
    return a+b+c

@calculater
def si(a,b,c):
    return (a*b*c)/100

def callin():
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    z=int(input("enter third number:"))
    print("addition:",add(x,y,z))
    print("simple interset:",si(x,y,z))

callin()