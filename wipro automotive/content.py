
with open("example.txt", "w") as file:
    file.write("Hello! Wipro \n")

with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)