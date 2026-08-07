"""
1. What is regular expression?
Regular expression are tools for manupulation string.

2. Why do we need regular expression?
-Verifying that strings match a pattern
-Performing substitutions in string

3. Regular expressions can be accessed using the re module
- match(): matches at the beginning of a string.
-search(): finds a match of a pattern anywhere in the string.
-findall(): returns a list of all substrings that match a pattern.
"""
# import re
# pattern = r'color'
# if re.match(pattern,'color is a color , I love red color'):
#     print('match')
# else:
#     print('Not matched')

# search method, je kuno 1ti te match korle match dekhabe
import re
pattern = r'color'
if re.search(pattern,'red is a color , I love red color'):
    print('match')
else:
    print('Not matched')


# findall() method
import re
pattern = r'color'
print(re.findall(pattern,'red is a color , I love red color'))