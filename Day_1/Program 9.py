def add(n1, n2):
    return n1+n2
    
def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2
    
def div(n1, n2):
    return n1/n2

def mod(n1, n2):
    return n1%n2
    
def exp(n1, n2):
    return n1**n2

def floor_div(n1, n2):
    return n1//n2
    

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
print("Addition: ",add(n1, n2))
print("Subtraction: ",sub(n1, n2))
print("Multiplication: ", mul(n1, n2))
print("Division: ", div(n1, n2))
print("Modulus: ", mod(n1, n2))
print("Exponent: ", exp(n1, n2))
print("Floor division: ", floor_div(n1, n2))
