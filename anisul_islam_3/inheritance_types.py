# Types of inheritance
# 1. Hierarchical Inheritance 
# 2. Multi-Level Inheritance
# 3. Multiple Inheritance

# 1. Hierarchical Inheritance 
# Shape
# a. Triangle b. Rentangle

# 2. Multi-Level Inheritance
# a. A 
# b. B 
# c. C

# 3. Multiple Inheritance
# A theke hoy B and C
# B and C theke hoy D


# 2. Multi-Level Inheritance dekhanu hoche
class A:
    def display1(self):
        print('I am inside A class')

class B(A):
    def display2(self):
        print('I am inside B class')

class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print('I am inside C class')

ob1 = C()
ob1.display3()