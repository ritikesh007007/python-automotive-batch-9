students =[100,90,80,70,60,50,40,30,20,10]
pass_students=[i if i>50 else "failed" for i in students]
print(pass_students)