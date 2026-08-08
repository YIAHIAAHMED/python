from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurant import Restaurant
from order import Order

mamar_restaurant = Restaurant('Mamar Restaurant')

def customer_menu():
    name = input("Enter Your Name: ")
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter your address: ')
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f'Welcome {customer.name}!!')
        print('1. View Menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. Pay bill')
        print('5. Exit')

        choice = int(input('Enter your choice: '))
        if choice == 1:
            customer.view_menu(mamar_restaurant)

        elif choice == 2:
            item_name = input('enter item name')
            item_quantity = int(input('enter item quantity'))
            customer.add_to_cart(mamar_restaurant, item_name, item_quantity )

        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.pay_bill()

        elif choice == 5:
            break
        else:
            print('Invalid Input')




def admin_menu():
    name = input("Enter Your Name: ")
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter your address: ')
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f'Welcome {admin.name}!!')
        print('1. Add new item')
        print('2. Add new empolyee')
        print('3. View employee')
        print('4. view items')
        print('5. Delete item')
        print('6. Exit')

        choice = int(input('Enter your choice: '))
        if choice == 1:
            item_name= input('Enter item name:')
            item_price = int(input('Enter price'))
            item_quantity = int(input('Enter item qty'))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurant, item)

        elif choice == 2:
            name =  input('enter emplyee name')
            phone =  input('enter phone num')
            email =  input('enter emplyee email')
            designation =  input('enter emplyee desigation')
            age =  input('enter emplyee age')
            salary =  input('enter emplyee salarty')
            address =  input('enter emplyee address')
            admin.add_employee(name, phone, email, address, age, designation, salary)
            employee = Employee(name, email, phone,address, age, designation, salary )

            admin.add_employee(mamar_restaurant, employee)
            

        elif choice == 3:
            admin.view_employee(mamar_restaurant)

        elif choice == 4:
            admin.view_menu(mamar_restaurant)

        elif choice == 5:
            item_name = input('Enter item name: ')
            admin.remove_item(mamar_restaurant, item_name)

        elif choice == 6:
           break
        else:
            print('Invalid Input')


while True:
    print('Welcome')
    print('1. customer:')
    print('2. Admin:')
    print('3. Exit:')
    choice = int(input('Enter your choice'))
    if choice ==1:
        customer_menu()
    elif choice ==2:
        admin_menu()
    elif choice ==3:
        break
    else:
        ('Invalid Input')



# mamar_res = Restaurant('Mamar Restaurant')
# mn = Menu()
# item = FoodItem('Pizza', 12, 10)
# item2 = FoodItem('Burger', 10, 30)
# admin = Admin('Rahim', 'r@gmail.com', 123333, 'Dhaka')
# admin.add_new_item(mamar_res,item)
# admin.add_new_item(mamar_res,item2)


# customer1 = Customer('Rahim', 'r@gmail.com', 123333, 'Dhaka')
# customer1.view_menu(mamar_res)

# item_name = input("Enter item name: ")
# item_quantity = int(input('Enter Item Quantity: '))

# customer1.add_to_cart(mamar_res, item_name, item_quantity)
# customer1.view_cart()