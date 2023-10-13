import tkinter as ttk
import random

def generate_pwd():
    length = text1.get()
    l = int(length)
    temp = ""
    letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    for i in range(l):
        char = random.randrange(1,3)
        if char == 1:
            element = random.choice(letters)
            temp += element
        elif char == 2:
            element = random.choice(numbers)
            temp += element
        else:
            element = random.choice(symbols)
            temp += element
    
    label3 = ttk.Label(text = f'New Password: {temp}')
    label3.place(x=10, y=150)



window = ttk.Tk()
window.title("Password generator")
window.minsize(450, 450)

label1 = ttk.Label(text = 'Password Generator', font = ('Algerian', 20))
label1.place(x=30, y=10)

label2 = ttk.Label(text = 'Enter length of password: ')
label2.place(x=10, y=70)

text1 = ttk.Entry()
text1.place(x=200, y=70)

button1 = ttk.Button(text = 'Generate password', command = generate_pwd)
button1.place(x=150, y=110)

window.mainloop()