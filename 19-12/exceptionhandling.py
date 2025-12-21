try:
    num = int(input("enter a number: "))
    result = 10 / num  
    
except ZeroDivisionError:
    print("the divisor cannot be 0")
except ValueError:
    print("invalid input! please enter a numeric value")
finally:
    print("execution completed")

print(f"result is {result}")