# Map & Filter Function
# def square(x):
#     return x*x
# num = [1,2,3,4,5]

# result = list(map(square, num))
# print(result)

# Filter Function
num = [1,2,3,4,5]
result = list(filter(lambda x: x%2==0, num)) # condition er sathe je gulu match korbena segulu remove kore dibe num theke
print(result)