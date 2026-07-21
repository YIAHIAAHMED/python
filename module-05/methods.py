# function likhi
def call():
    print('calling someone i dont know')
    return 'call done'



class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms): # prothom ti sobsomoy string mone kore python e jonne dite hoy
        text = f'sendin SMS to: {phone} and message: {sms}'
        return text

# object banai feli
my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(41524, 'I forgot to miss you')
print(result)


