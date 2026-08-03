# stack 
# push er mane stack e data rakha
# pop er mane stack theke data remove kora

# stack kaj kore last in first out

# books = []
# books.append('Learn C')
# books.append('Learn C++')
# books.append('learn python')
# # print(books)
# books.pop()
# print(books[-2])

# if not books:
#     print('no books left')
# else:
#     print('books have')



# queue examples
# queue kaj kore first in first out

from collections import deque
bank = deque(['yiahia', 'anis', 'Karim'])
# print(bank)
bank.popleft()
bank.popleft()
bank.popleft()
print(bank)

if not bank:
    print('no person left')