def abc():
    yield 1
    yield 2
    yield 3
for value in abc():
    print(value)
    
#yield keyworf make a def/func to convert it into enretaer