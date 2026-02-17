# Application Module (Unit to Test)
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

class Calculator:
    def multiply(self, a, b):
        return a * b
