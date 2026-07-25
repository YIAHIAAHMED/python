def timer(func):
    def inner():
        print('time started')
        func()
        print('time started')
    return inner

#timer()()
 
@timer # eta decorator
def get_factorial():
    print('factorial starting')

get_factorial()

# or timer(get_factorial)() jodi @timer na dite chai



# factorial uses way
import math
import time
def timer(func):
    def inner(*args, **kwargs):
        print('time started')
        start = time.time()
        func(*args, **kwargs)
        print('time started')
        end = time.time()
        print(f'total time taken: {end - start} seconds')
    return inner

#timer()()
 
@timer # eta decorator
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factorial of {n} is: {result}')

get_factorial(n=12)