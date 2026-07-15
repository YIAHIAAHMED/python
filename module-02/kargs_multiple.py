def full_name (first, last):
    name = f'Full name is :{first} {last}'
    return name

# name = full_name('Alu', 'kodu')
name = full_name(last='kodu', first='Alu' )
print(name)

#def famous (**kargs)
def famous_name (first, last, **addition):
    name = f'{first} {last}'
    #print (addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first='taher', last='Ali', title="Hujur", title2='shayokh', last2='taheri')

#def function_name (num1, num2, *args, **kargs):

# return multiple things from an array
def a_lot(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    #return [sum, mult, remain]
    return sum, mult, remain

Everything = a_lot(55, 21)
print(Everything)
