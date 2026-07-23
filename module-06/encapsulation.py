# encapsulation er mane --> hide details
# access modifirer: public, protected, private
class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name # public attribute
        # self.balance = initial_deposit
        self.__balance = initial_deposit

    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance # erokom under score double hole seta private hoy
    # r 1 ti under score thakle seta protected dhora hoy
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Fokira taka nai'

rafsun = Bank('Choto bro', 10000)
print(rafsun.holder_name)
# rafsun.balance = 0
# print(rafsun.balance)
rafsun.holder_name = 'boro bai'
rafsun.deposit(40000)

print(rafsun.get_balance())
print(rafsun.holder_name)
# print(dir(rafsun))
print(rafsun._Bank__balance)

    