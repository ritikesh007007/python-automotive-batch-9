'''3 manager and 12 members
ex -manager m1:employee
one empoyee cannot report to 2 managers 
use filter, lambda, reduce . '''

from functools import reduce


managers = ["Ratan Tata", "Aman mishra", "Satya Nadella"]
employees = [
    "Hritik ", "Priya ", "Sushma", "Rakesh", 
    "Vikash ", "Smridhi", "Ritikesh", "Anil", 
    "Saurabh", "Pooja ", "Kartik", "Neha"
]


assignments = reduce(
    lambda acc, i_emp: (
        acc[0] + [i_emp[1]] if i_emp[0] % len(managers) == 0 else acc[0],
        acc[1] + [i_emp[1]] if i_emp[0] % len(managers) == 1 else acc[1],
        acc[2] + [i_emp[1]] if i_emp[0] % len(managers) == 2 else acc[2],
    ),
    enumerate(employees),
    ([], [], [])
)


result = [
    {"manager": managers[0], "employees": assignments[0]},
    {"manager": managers[1], "employees": assignments[1]},
    {"manager": managers[2], "employees": assignments[2]}
]


for assignment in result:
    print(f"{assignment['manager']}: {assignment['employees']}")
