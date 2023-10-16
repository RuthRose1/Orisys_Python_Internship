import re

def phone_valid(phno):
    pattern = "[(]?\d{3}[)]?[-]?\s?\d{3}[-]?\d{4}"
    return re.match(pattern, phno)
    

flag = 0
while (flag == 0):
    print("Phone number Validation")
    print("1. Check phone number\n2. Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        phno = input("Enter phone number: ")
        if phone_valid(phno):
            print("Phone number is valid\n")
        else:
            print("Phone number is invalid\n")
    elif ch == 2:
        flag = 1
    else:
        print("Invalid input")