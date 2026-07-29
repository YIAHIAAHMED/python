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

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            item.quantity = quantity
            self.cart.add_item(item)
            print('Item added')
        else:
             print('Item not found')

    def view_cart(self):
         print('**View Cart**')
         print('Name\tPirce\tQuantity')
         for item, quantity in self.cart.items.items():
              print(f'{item.name} {item.price} {item.quantity}')
         print('Total Price:{self.cart.total_price}')

class Order:
    def __init__(self):
         self.items = {}

    def add_item(self, item):
        if item in self.items:
             self.items[item] += item.quantity # jodi item ta cart e already thake
        else:
             self.items[item] = item.quantity # jodi cart e na thake

    def remove(self, item):
         if item in self.items:
              del self.items[item]

    def total_price(self):
         return sum(item.price * quantity for item, quantity in self.items.item())
    
    def clear(self):
         self.items = {}
         


             


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

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)
        

class Restaurant:
     def __init__(self, name):
          self.name = name
          self.employees = [] # eta hocche amader database
          self.menu = FoodItem()

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
item2 = FoodItem('Burger', 10, 30)
mn.add_menu_item(item)
mn.add_menu_item(item2)
mn.show_menu()

