def choice(num):
    def calculate(func):
        def inner(a, b):
            if num == 1:
                print("addition of two number:")
            elif num == 2:
                print("subtraction of two number:")
            elif num == 3:
                print("multiplication of two number:")
            elif num == 4:
                print("division of two number:")
            print(func(a, b))  
        return inner
    return calculate  

@choice(1)
def add(a, b):
    return a + b

@choice(2)
def sub(a, b):
    return a - b

@choice(3)
def mul(a, b):
    return a * b

@choice(4)
def div(a, b):
    return a / b

def input_num():  
    x = int(input("enter first number:"))
    y = int(input("enter second number:"))
    
    print("\nChoose operation:")
    print("1. Add  2. Sub  3. Mul  4. Div")
    ch = int(input("Enter choice (1-4): "))
    
    if ch == 1:
        add(x, y)
    elif ch == 2:
        sub(x, y)
    elif ch == 3:
        mul(x, y)
    elif ch == 4:
        div(x, y)

input_num()
