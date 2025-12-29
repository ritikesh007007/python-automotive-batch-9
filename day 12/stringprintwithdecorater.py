def decorater(func):
    def inner():
        result =func()
        return "****" + result + "****"
    return inner

@decorater
def greet():
     return "welcome"
 
print(greet())