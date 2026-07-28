# Users
# 1.Customer
# 2. Employee
# 3. Admin

from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Employee('rahim', 'rahim@gmail.com', 1299, 'Dhaka', 23, 'chef', 12000)
# print(emp.name)
        
class Admin(User):
    def __init__(self, name, phone, email, address):
            super().__init__(name, phone, email, address)
            self.employee = [] # eta hocche amader database

    def add_employee(self, name, email, phone, address):
         employee = Employee(name, email, phone, address)