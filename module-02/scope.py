#glabal variable, you can access galabal variabale without using the global keyword, but if you want to modiy a global variable, you have to use the global 
balance = 3000

def buy_things (item, price):
    global balance
    print(f'previous balance', balance)
    balance = balance-price
    print ('balance after buying {item}', balance)

buy_things('sunglass', 1000)
print('global balcane after buy', balance)