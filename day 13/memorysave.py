def large_num(n):
    for i in range(n):
        yield i
gen=large_num(100)
print(next(gen))
print(next(gen))
print(next(gen))

#basuc list compreshension
list=[x*x for x in range(5)]
print(list)

#doinf comprehension usnig generator
gen1=(x*x for x in range(5))
print(gen1)