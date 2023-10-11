#1st define function then call the function
def calculator(n1, n2):
    flag = 0
    print('\tMenu\n1. Add\n2. Subtract\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponent\n7. Floor division\n8. Exit')
    flag = 0
    while(flag == 0):
        ch = int(input("Enter operation: "))
        if ch == 1:
            print("Addition:", n1+n2)
        elif ch == 2:
            print("Subtraction:", n1-n2)
        elif ch == 3:
            print('Multiplication:', n1*n2)
        elif ch == 4:
            print('Division:', n1/n2)
        elif ch == 5:
            print('Modulus:', n1%n2)
        elif ch == 6:
            print('Exponent:', n1**n2)
        elif ch == 7:
            print('Floor division:',n1//n2)
        elif ch == 8:
            flag = 1


n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
calculator(n1, n2)