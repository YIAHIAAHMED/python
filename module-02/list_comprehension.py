numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
odds=[]
for num in numbers:
    if num%2==1 and num % 5==0:
        odds.append(num)

print(odds)

# odds_num = [num for num in numbers if num %2 ==1 ]
odds_num = [num for num in numbers if num %2 ==1 if num % 5 ==0 ] # ei dui ta hizi bizi erokom na kora valo

print(odds_num)

players =['sakib', 'musfik', 'mustafiz']
ages =[38, 38, 32]

age_comb = []
for player in players:
    print('player:', player)
    for age in ages:
        print(player, age)
        age_comb.append([player, age])
print(age_comb)