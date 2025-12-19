from addition import addition
from multiple import multiplication


m = float(input("Money: "))
r = float(input("Rate (%): ")) / 100
t = float(input("Time: "))

si = multiplication(m, addition(1, multiplication(r, t)))
print(f"Interest: ₹{si:.2f}")
