# Run time error
# num2 = int(input('Enter a number: ')) # enter 0 dile exception asbe or int na dile
# result = 20 /num2
# print(result)
# print('Done')

# text = 'Yiahia'
# print(text[8])
# print('Done')

#exception handle ei ongsho try: er under e rakhte hobe
# try:
#     list = [20, 0, 30]
#     # result = list [0] / list[1]
#     # result = list [0] / list[2]
#     result = list [0] / list[3]
#     print(result)
# except ZeroDivisionError:
#     print('Dividing by zero is not possible')
# # except IndexError:
# #     print('Index eroor')

# finally:
#     print('Successful')



# try:
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
    
#     result = num1 / num2
#     print(result)
# except ZeroDivisionError, ValueError:
#     print('Dividing by zero is not possible')


# finally:
#     print('Successful')

def voter (age):
    if age< 18:
        raise ValueError('Invalid Voter')
    return 'You are allowed to vote'

try:
    # print(voter(19))
    print(voter(17))
except ValueError as e:
    print(e)