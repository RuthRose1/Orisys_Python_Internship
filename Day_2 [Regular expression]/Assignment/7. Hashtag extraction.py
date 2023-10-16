import re

text = '''
GeeksforGeeks is a wonderful #website for #ComputerScience
This day is beautiful!#instagood #photooftheday #cute
'''

pattern = "[#]\w*"
print(re.findall(pattern, text))