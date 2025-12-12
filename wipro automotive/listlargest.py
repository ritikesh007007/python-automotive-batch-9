numbers = [31, 12, 53, 20, 9]

big = numbers[0]

for x in numbers:
    if x > big:
        big = x

print("Largest is:", big)