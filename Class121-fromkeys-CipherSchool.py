# fromkeys

# d = {'name' : 'unknown' , 'age' : 'unknown' }
# d= dict.fromkeys(('name' , 'age' , 'height'), 'unknown')
# d= dict.fromkeys("abc", 'unknown')
# d= dict.fromkeys(range(1,11), 'unknown')
# d= dict.fromkeys(['name' , 'age'], 'unknown')
# print(d)





d={'name': 'unknown', 'age': 'unknown'}
# print(d['name'])
# print(d.get('name'))
# print(d.get('names'))

if d.get('name'):
    print("present")
else:
    print("not present")



# copy
d1= d.copy()
# print(d1)

print(d1==d)
print(d1 is d)

