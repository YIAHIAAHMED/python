class Shop:
    cart = [] # cart is a class attribute, egulu sob gulur sathe share hoye jay
    def __init__(self, buyer): # this is class atribute
        self.buyer = buyer

    def add_to_cart(self, item):  # this is method
        self.cart.append(item)

mehzabeen = Shop('meh jabeen')
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('phone')
print(mehzabeen.cart)

nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)