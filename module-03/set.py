# list use korbo []
# tuple use korbo ()
# set use korbo {}
# set : unique items collection, no duplicate, order or sequence maintain kore na
numbers = [12, 56, 98, 78, 56, 12, 6, 98]
print(numbers)
numbers_set = set(numbers)
# print(numbers_set)
numbers_set.add(55)
print(numbers_set)
# add or remove kore jabe but numbers_set[1]=5 erokom kora jabe na
numbers_set.remove(6)
print(numbers_set)
for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print('9 exists')
if 98 in numbers_set:
    print('98 exists')

A ={1,3,5,7}
B = {1,2,3,4,5}
print(A&B) # etate komon dekhabe
print(A|B) # etate sob dekhabe A U B er moto