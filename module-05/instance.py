class Shop:
    Shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute eta share hoy na sobar sathe

    def add_to_cart(self, item):
        self.cart.append(item)
mehjabeen = Shop('Mez jab een')
mehjabeen.add_to_cart('shoe')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)

nisho = Shop('nishi night er')
nisho.add_to_cart('hat')
nisho.add_to_cart('watch')
print(nisho.cart)

apurovo = Shop('age to ')
apurovo.add_to_cart('chiruni')
print(apurovo.cart)
