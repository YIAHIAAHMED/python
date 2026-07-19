#lambda

# def doubled (x):
#     return x*2

#or
doubled = lambda num: num * 2
squared = lambda num : num * num

result = doubled(44)
output = squared(9)
# print(result, output)

add = lambda x, y: x + y
sum = add (11, 33)
# print(sum)

numbers = [ 12, 56, 98, 78, 56, 12, 6, 98]
doubled_nums = map(doubled, numbers)
#or doubled_nums = map(lambda x: x*2, numbers)
# print(doubled_nums)
squared_nums = map(lambda x: x*x, numbers)
# print(list(doubled_nums))
print(list(squared_nums))
