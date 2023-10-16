import re

password = input('Enter password: ')

pattern = '(?=^.{8,}$)(?=.*\d)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
correct_pwd = re.findall(pattern, password)
if correct_pwd == []:
    print("Password id not strong")
else:
    print("Password is strong")