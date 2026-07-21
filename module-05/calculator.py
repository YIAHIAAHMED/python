class Calculator:
    brand = 'Casio MS990'

    def add(self, num1, num2):
        return num1 + num2
    
    def deduct(self, num1, num2):
        return num1 - num2
    
    def multiple(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        return num1 / num2


    # add method
    # deduct method
    # multiply method
    # divide method

# Object toiri kora
cal = Calculator()
print(cal.brand)
print(cal.add(10,5))
print(cal.deduct(10,5))
print(cal.multiple(10,5))
print(cal.divide(10,5))


