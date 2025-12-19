# 20 students - find same first name, different surname

students = [
    ("Ritik", "Sharma"), ("Ravi", "Kumar"), ("Shiva", "Gupta"), ("Shivam", "Kumar"),
    ("Mohan", "Singh"), ("Geeta", "Yadav"), ("Amit", "Patel"), ("Priya", "Singh"),
    ("Rahul", "Sharma"), ("Pooja", "Verma"), ("Anil", "Kumar"), ("Sunita", "Gupta"),
    ("Vikash", "Yadav"), ("Neha", "Patel"), ("Deepak", "Singh"), ("Ritu", "Sharma"),
    ("Karan", "Gupta"), ("Meera", "Verma"),("Ritik", "Verma") , ("Lata", "Yadav")
]


# Find first duplicate
for i in range(19):  # Check 20 students
    name1 = students[i][0]
    surname1 = students[i][1]
    
    for j in range(i+1, 20):  # Compare with remaining students
        name2 = students[j][0]
        surname2 = students[j][1]
        
        if name1 == name2 and surname1 != surname2:
            print(f"Found: {name1} {surname1} and {name2} {surname2}")
            exit()  