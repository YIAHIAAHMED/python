# sub(pattern, replace, string)
import re
pattern = r'colour'
text1 = 'My favourite colour is red. I Love blue colour as well'
# text2 = re.sub(pattern, 'color', text1)
text2 = re.sub(pattern, 'color', text1, count=1)
print(text2)