class Dog:  
    #first we  define the common and then the qunique
    def __init__(self, name, age):  #_init_ methhod that can also be a constructor that runs everytime an object is created 
        self.name=name #jemmy
        self.age=age #11
        
        #Dog has barking behaviour of the parent class
    def bark(self):
            #attributes unique
     return f"{self.name} say woof!"
        
        
Dog1=Dog("jemmy",11)     
Dog2=Dog("tommy",5)
#as per requirement we can create any number of objects   

print(Dog1.bark())
print(Dog2.bark())