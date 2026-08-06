# File reading file.txt
# r = read kora
# w = write kora
# r+ = read and write kora
# from pathlib import Path
# file = open("file.txt","r")
# print(file.readable())
# file.close()

# file = open("anisul_islam_2/file.txt", "r+") # anisul_islam_2 eta disi jehetu python3 anisul_islam_2/file.py erokom dichi
# print(file.readable())

# text = file.read()
# print(text)

# size = len(text)
# print(size)
# file.close()

# list e rakhte chaile
# text = file.readlines()[0]
# # text = file.readlines()[1]
# # text = file.readlines()[2]
# print(text)
# file.close()

# for loop er madhome
# for line in file:
#     print(line)

# file.close()


# append korar jonne 'a' use korte hoy
file = open("anisul_islam_2/file.txt", "w")

file.write('\nSadi - lecturer of physics')

file.close()

