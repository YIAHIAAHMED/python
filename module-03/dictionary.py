numbers =[12, 56, 98, 78, 56, 12, 26, 98]
person1 = ['kala chan', 'kalipur', 23, 'student']
# key value pair
# dictinary
# object
# hash table
# overlap with set
person = {'name': 'kala pakhi', 'address' : 'Kaliapur', 'age': 23, 'job': 'bekar'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
print(person)

# special dictionary looping
for key, value in person.items():
    print(key, value)