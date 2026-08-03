# set e item gulur kono order thake na
# index diye value gulu access kora jabe na
# kono duplicate value rakha jabe na
# curly brakets or set function use kora jabe

# num = {1, 2, 3, 4, 5, 5} # output 5 dekhabe na 2 bar
# print(num)

# Onno system
# num1 = {1, 2, 3, 4, 5 }
# num2 = set([4,5,6])
# num2.add(7)
# num2.remove(7)
# # print(num2)
# print(7 in num2) # 4 num2 er modde ache naki check kora

# set er real uses

num1 = {1, 2, 3, 4, 5 }
num2 = set([4,5,6,7])

# print(num1 | num2)  # union set er sign | , eta dile num1 and num2 er sob man dekhabe

# print(num1 & num2)  # intersection set er sign & , eta dile num1 and num2 er common man dekhabe


print(num1 - num2)  # difference set er sign - , eta dile num1 and num2 er modde je gulu komon seta num1 theke bad diye num1 er baki gulur man dekhabe