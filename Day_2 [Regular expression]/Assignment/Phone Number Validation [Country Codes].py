import re

def phone_valid(phno):
    pattern = "[(]?\d{3}[)]?[-]?\s?\d{3}[-]?\d{4}"
    return re.match(pattern, phno)

def check_country_code(chk_cc):
    cc = {'+971':'UAE',
          '+91': 'India',
          '+1': 'US',
          '+86': 'China',
          '+44': 'UK'}
    if chk_cc in cc.keys():
        print(f'Country code exists. The country code {chk_cc} belongs to {cc[chk_cc]}')
        return 1
    else:
        print('Country code is not found')
        op = input("Does country code exist(y/n): ")
        if op.lower() == 'y':
            new_cc = input(f'Enter country of country code of {chk_cc}: ')
            cc[chk_cc]= new_cc
            return 1
        else:
            return 0
     


flag = 0
l = 0
found = 0
while (flag == 0):
    print("Phone number Validation")
    print("1. Check phone number\n2. Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        phno = input("Enter phone number: ")
        for i in phno:
            if i.isnumeric():
                l +=1
        if l == 10:
            if phone_valid(phno):
                print("Phone number is valid\n")
        elif l<10:
            print("Phone number is invalid\n")
        elif l>10:
            if phno[0] == '+':
                no_cc = l-10
                print(l)
                #To check if country code is valid
                chk_cc = phno[0:no_cc+1]
                if check_country_code(chk_cc)== 1:
                    print("Country code is valid\n")
                    found = 1
                else:
                    found = 0
                # To check if phone number is valid
                if found == 1:
                    pho_no = phno[no_cc:l]
                    if phone_valid(pho_no):
                        print("Phone number is valid\n")
                    else:
                        found = 0
                if found == 0:
                    print("Phone number is invalid\n")
            elif phno[0] != '+':
                print("Phone number is invalid\n")
    elif ch == 2:
        flag = 1
    else:
        print("Invalid input")