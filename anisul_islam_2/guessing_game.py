"""
1. start
2. input guessNumber
3. Generate random number
4. if guessNumber == randonNumber
    i) yes, print won
    ii) No, print lost
5. End

"""
# from random import randint
# guessNumber = int(input('Enter your guess between 1 to 5: '))
# randomNumber = randint(1, 5)
# if guessNumber == randomNumber:
#     print('You have won')
# else:
#     print('You have lost')
#     print('randon number was:',randomNumber)

# for loor er modde diye

for x in range(1, 6):
    from random import randint
    guessNumber = int(input('Enter your guess between 1 to 5: '))
    randomNumber = randint(1, 5)
    if guessNumber == randomNumber:
        print('You have won')
    else:
        print('You have lost')
        print('randon number was:',randomNumber)