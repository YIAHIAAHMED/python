# list user theke input neyar jonne

# n = input('Enter a text of numbers: ') # 10 20 30 40
# list = n.split() # er maddome 10, 20, 30, 40 alada hpbe, eta string input hoy
# sum = 0
# for num in list:
#     sum = sum + int(num) # int e convert korte hoy
# print(sum)


# string input nibo user theke
numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input('Enter a text of numbers: ') # my name is 123

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z': # text naki check
        numOfLetters = numOfLetters + 1

    elif x >= '0' and x <= '9': # digit naki check
        numOfDigits = numOfDigits + 1

    elif x == ' ': # word naki check, space paile word 
        numOfWords = numOfWords + 1

    
print('digits', numOfDigits)
print('letters', numOfLetters)
print('words', numOfWords + 1)
