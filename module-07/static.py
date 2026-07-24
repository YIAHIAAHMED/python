class Shopping:
    cart = [] # class attribute , static attribute
    origin = 'china'
    
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def purchase (self, item, price, amount):
        remaining = amount - price
        price(f'buying: {item} for price: {price} remainging: {remaining}')

    def hudai_dehi(self, item):
        print('hudai dekhi kinmu na', item)

# Shopping.purchase( 2, 3, 4)
basundara = Shopping('basu en dhara', 'not popular')
basundara.purchase('lungi', 500, 1000)
