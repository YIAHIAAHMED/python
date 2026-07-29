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
            

    def add_employee(self, restaurant, empolee):
         restaurant.add_employee(empolee)

    def view_employee(self, restaurant):
         restaurant.view_employee()
        

class Restaurant:
     def __init__(self, name):
          self.name = name
          self.employees = [] # eta hocche amader database

     def add_employee(self, employee):
         self.employees.append(employee)

     def view_employee(self):
         print('Employee List!!')
         for emp in self.employees:
              print(emp.name, emp.email, emp.phone, emp.address)

class Menu:
    def __init__(self):
          self.items = [] # items er database

    def add_menu_item(self, item):
         self.items.append(item)

    def find_item(self, item_name):
          for item in self.items:
               if item.name.lower() == item_name.lower():
                    return item
          return None
     
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted")
        else:
             print('Item not found') 

    def show_menu(self):
        print('******Menu*******')
        print('Name\tPrice \t Quantity')     
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
               
class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
             
                    


mn = Menu()
item = FoodItem('Pizza', 12, 10)
mn.add_menu_item(item)
mn.show_menu()

