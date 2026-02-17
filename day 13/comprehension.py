#dict comprehension
d={num:num*2 for num in range(1,4)}

states = ['kerala','tamilnadu','karnataka']
capitals = ['thiruvananthapuram','chennai','bangalore']
di ={states:capitals for states,capitals in zip(states,capitals)}

#set
a=[1,2,3,4,5,1,2,3]
sc={n for n in a if n%2 ==0}
print(sc)
