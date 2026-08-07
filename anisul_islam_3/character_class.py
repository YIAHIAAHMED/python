# character class
# import re
# pattern = r'[aeiou]'

# if re.match(pattern,'ebbbe'): # je kuno 1 ti prothome match korle hobe jaha disi
#     print('Matched')
# else:
#     print('Not Matched')

# A-Z porjonto hole hobe
# import re
# pattern = r'[A-Z]'

# if re.match(pattern,'Xbbbe'): 
#     print('Matched')
# else:
#     print('Not Matched')

# all porjonto hole hobe   but sequence maintain korte hobe
import re
pattern = r'[A-Z][a-z][0-9]'

if re.match(pattern,'Ae1'):
    print('Matched')
else:
    print('Not Matched')