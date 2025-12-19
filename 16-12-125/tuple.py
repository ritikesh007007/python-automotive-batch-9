#tuple - the collection which is ordered and unordered, unchangeable , allows duplicate members and used to group together related data

student = ("bro", 21, "male")
print(student.count("bro"))
print(student.index("male"))

for i in student:
    print(i)
    
if "bro" in student:
    print("bro is present")    