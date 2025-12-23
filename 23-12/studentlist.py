
# Parent Class 
import re
class Person:
    def __init__(self, name):
        # Encapsulation
        self.name = name

    #  (Polymorphism)
    def get_role(self):
        return "I am a Person"
    
# Child Class Student (Inheritance)
class Student(Person):
    def __init__(self, student_id, name):
        
        super().__init__(name)

        self.student_id = student_id

    def extract_id_number(self):
      
        parts = self.student_id.split("_")
        number = int(parts[1])
        return number

    # Polymorphism: method overriding
    def get_role(self):
        return "I am a Student"

    def display_details(self):
        print("Student ID   :", self.student_id)
        print("Student Name :", self.name)
        print("Role         :", self.get_role())


#  List of 10 students (list of tuples)
students_data = [
    ("std_001", "Aarav"),
    ("std_002", "Bhavya"),
    ("std_003", "Charan"),
    ("std_004", "Diya"),
    ("std_005", "Eshan"),
    ("std_006", "Farah"),
    ("std_007", "Gopal"),
    ("std_008", "Hina"),
    ("std_009", "Ishaan"),
    ("std_010", "Jiya")
]

#  Convert tuple data into Student objects
students_list = []

for data in students_data:
    sid = data[0]
    name = data[1]

    student_obj = Student(sid, name)
    students_list.append(student_obj)


even_id_students = []
odd_id_students = []

for student in students_list:
    id_number = student.extract_id_number()

    if id_number % 2 == 0:
        even_id_students.append(student)
    else:
        odd_id_students.append(student)

#  (Even IDs)
print("==============================================")
print("Students Allowed to Participate FIRST (Even IDs)")
print("==============================================")

for student in even_id_students:
    student.display_details()
    print("----------------------------------------------")

#  (Odd IDs)
print("\n==============================================")
print("Students Allowed to Participate NEXT (Odd IDs)")
print("==============================================")

for student in odd_id_students:
    student.display_details()
    print("----------------------------------------------")