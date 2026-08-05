# Recursion is a process where a function can call itself.
# To stop calling we need a base case.

# Two imlrrtant points in case of recursion
# a. Recusive call
# b. base case

# example
# 5! = 5*4*3*2*1
# 4! = 4*3*2*1
# 3! = 3*2*1
# 2! = 2*1
# 1! = 1
# n! = n*(n-1)!

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
result = fact(5)
print(result)
