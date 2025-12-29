#decorators in Python
def changecase(func):
    def myinner():
        return func().upper()
    
    return myinner
#calling decorator

@changecase

def myfunc():
    return "hello world"

print(myfunc())


def upper(func):
    def big():
        return func().upper()
    return big
@upper
def greet():
    return "hello world"
print(greet())
    
    
    
    
    
    
    
    
    
    
    
    
  