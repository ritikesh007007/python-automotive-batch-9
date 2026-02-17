#dictonary-- it is a changable , unordered collection of unique key:value 

capitals={'India':'New Delhi',
            'USA':'Washington DC',
            'UK':'London',
            'France':'Paris',
            'Germany':'Berlin'}

print(capitals['India'])
print(capitals.get('China'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'Australia':'Canberra'})
capitals.update({'India':'Mumbai'})
capitals.pop('Germany')


for key,value in capitals.items():
    print(f"{key} {value}")
    
capitals.clear()