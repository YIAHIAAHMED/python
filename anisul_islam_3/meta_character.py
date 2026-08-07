"""
meta character
. (dot)(any character)
^$
*(0 or more)
+(1 or more)
?(0 or 1)
{and}
"""
# import re
# pattern = r'colo.r' # . mane je kuno character ke match korbe
# if re.match(pattern, 'colour'):
#     print('Matched')


# import re
# pattern = r'^colo.r$' # ^ mane shurute co thakbe and $ mane shese r thakbe

# if re.match(pattern, 'colouar'):
#     print('Matched')


# import re
# pattern = r'a*' 

# if re.match(pattern, 'qqqcolouar'):
#     print('Matched')


# import re
# pattern = r'a+' # mane a kompokke 1 bar thakbe

# if re.match(pattern, 'a'):
#     print('Matched')

# import re
# pattern = r'a+b' # mane ab kompokke 1 bar thakbe

# if re.match(pattern, 'ab'):
#     print('Matched')

# import re
# pattern = r'(-)?icecream' 

# if re.match(pattern, '-icecream'):
#     print('Matched')


import re
pattern = r'a{1,3}&' # 1, 3 mane a 1-3 ti thakle hobe

if re.match(pattern, 'aaa&'):
    print('Matched')