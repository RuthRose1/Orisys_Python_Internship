import re

def mail_valid(mail):
    pattern = re.compile("\w*@(?!hotmail|yahoo)\w*.*[org|com|in]")
    return re.match(pattern, mail) 

flag = 0
while (flag == 0):
    print("Mail Validation")
    print("1. Check mail\n2. Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        mail = input("Enter mail: ")
        if mail_valid(mail):
            print("Mail is valid\n")
        else:
            print("Mail is invalid\n")
    elif ch == 2:
        flag = 1
    else:
        print("Invalid input")
