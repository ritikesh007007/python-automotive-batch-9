myString="abcdef#ghijkl"
sub1=myString[0:6] #slice the first 7 elements
sub2=myString[7:] #from the 7th element till end
sub3=myString[:5] #first 6 elemets
sub4=myString[10] #the 10th elemetns - index from 0
sub5=myString[-5] #last 5 elements

if "a" in myString:
    print("a is there")
    
word=myString.split("#")
print(word)
#append is used in list, collection and avoid in string

myString=myString+"m"
print(myString)
#the above string is not same and a new string created 
#string is immutable in python