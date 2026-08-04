# Lamda
# 1. A function without name (Anonymous Function)
# 2. Not powerful as Named Functio
# 3. It can work with single expression/ single line of code

# this named function
def calculatte(a,b):
    return a*a + 2*a*b + b*b

print(calculatte(2,3))


# this is without named function (lamda)
print((lambda a,b : a*a + 2*a*b + b*b) (2,3))

# or

a = (lambda a,b : a*a + 2*a*b + b*b) (2,3)
print(a)

# cube 
def cube (x):
    return x*x*x

# lamda
a = (lambda x : x*x*x) (3)
print(a)



