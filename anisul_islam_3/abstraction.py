# OOP Holo
"""
1. class
2. object 
3. Inheritance
4. Abstraction
5. Encapsulation
6. Polymorphism

"""
# 4. Abstraction mane import kora ABC, abstractmethod

from abc import ABC, abstractmethod
class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass

class Triangle (Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print('area triangle', area)

class Rectangle (Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print('area rectangle', area)


t1 = Triangle(20,30)
t1.area()

r1 = Rectangle(20,30)
r1.area()
