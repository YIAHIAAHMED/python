# def student (id,name):
#     # print(id, name)

# student(101, 'yiahia')


# parameter er sonkha same rekhe function kaj korar jonne
# sudhu * ei sign dile hobe

# def student(*details):
#     print(details)

# student(101, 'Yiahia')
# student(102, 'Yiahia', 3.75)


# def student(*details):
#     print(details[0]) # erokom index diye access kora jabe

# student(101, 'Yiahia')
# student(102, 'Yiahia', 3.75)

# def add(*numbers):
#     sum = 0
#     for num in numbers:
#         sum = sum + num 
#     print(sum)

# add(10,20)
# add(10,20,30)
# add(10,20,30,40)
# add(10,20,30,40,50)



# xxargs
# eta diye dictionary er moto key and value pass kora jabe
def student(**details):
    # print(details)
    print(details['id'])


student(id=101, name='Yiahia')