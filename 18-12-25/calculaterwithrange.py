start = int(input("Enter start: "))
end = int(input("Enter end: "))
total = 0
#addition
for num in range(start, end + 1):
    total += num
print(f"Sum: {total}")
total = 0
#substraction
for num in range(start, end + 1):
    total -= num
print(f"Subtraction result: {total}")
total = 1
#multiplication
for num in range(start, end + 1):
    total *= num
print(f"Multiplication result: {total}")
