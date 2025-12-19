print("get max,min swap value of variables")
print("\n 1.Max \n 2.Min \n 3.Swap")
a,b=map(int,input("Enter two values:").split(","))
choice = int(input("Enter your choice:"))
if(choice==1):
    print(max(a,b))
elif(choice==2):    
   print(min(a,b))
elif(choice==3):   
    a,b=b,a
    print("After swaping %d %d "%(a,b))
else:
    print("Invalid choice")