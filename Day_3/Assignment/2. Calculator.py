import tkinter as ttk

cal = ''

def add_add():
    global cal
    element = button1.cget("text") #To get the text of the button
    cal += element
    text1.insert('end', element) #'End' was given so the calculator writes from left to right, if 0 is given it write from right to left

def add_sub():
    global cal
    element = button2.cget("text")
    cal += element
    text1.insert('end', element)
    
def add_mul():
    global cal
    element = button3.cget("text")
    cal += element
    text1.insert('end', element)

def add_div():
    global cal
    element = button4.cget("text")
    cal += element
    text1.insert('end', element)

def add_1():
    global cal
    element = button5.cget("text")
    cal += element
    text1.insert('end', element)

def add_2():
    global cal
    element = button6.cget("text")
    cal += element
    text1.insert('end', element)

def add_3():
    global cal
    element = button7.cget("text")
    cal += element
    text1.insert('end', element)

def add_4():
    global cal
    element = button8.cget("text")
    cal += element
    text1.insert('end', element)

def add_5():
    global cal
    element = button9.cget("text")
    cal += element
    text1.insert('end', element)

def add_6():
    global cal
    element = button10.cget("text")
    cal += element
    text1.insert('end', element)

def add_7():
    global cal
    element = button11.cget("text")
    cal += element
    text1.insert('end', element)

def add_8():
    global cal
    element = button12.cget("text")
    cal += element
    text1.insert('end', element)

def add_9():
    global cal
    element = button13.cget("text")
    cal += element
    text1.insert('end', element)

def add_0():
    global cal
    element = button14.cget("text")
    cal += element
    text1.insert('end', element)

def calculate():
    global cal
    element = button16.cget("text")
    text1.insert('end', element)
    l = len(cal)
    sy = res = 0
    for i in range(0, l):
        if cal[i] == '+' or cal[i] == '-' or cal[i] == '*' or cal[i] == '/':
            sy = i

    c = result = 0
    num1= cal[0:sy]
    num2 = cal[sy+1:l]
    if num1 and num2:  
        n1 = int(num1)
        n2 = int(num2)
        
    if cal[sy] == '+':
        res = n1 + n2
    elif cal[sy] == '-':
        res = n1 - n2
    elif cal[sy] == '*':
        res = n1 * n2
    elif cal[sy] == '/':
        res = n1 / n2
    text1.insert('end', res)
    
def clear_cal():
    global cal
    text1.delete(0, 'end')
    cal = ''
    
        

window = ttk.Tk()
window.title("Calculator")
window.minsize(20, 270)

text1 = ttk.Entry(width = 22)
text1.place(x=10, y=10)

button1 = ttk.Button(text = '+', command = add_add)
button1.place(x=40, y=50)

button2 = ttk.Button(text = '-', command = add_sub)
button2.place(x=70, y=50)

button3 = ttk.Button(text = '*', command = add_mul)
button3.place(x=100, y=50)

button4 = ttk.Button(text = '/', command = add_div)
button4.place(x=130, y=50)

button5 = ttk.Button(text = '1', command = add_1)
button5.place(x=40, y=90)

button6 = ttk.Button(text = '2', command = add_2)
button6.place(x=70, y=90)

button7 = ttk.Button(text = '3', command = add_3)
button7.place(x=100, y=90)

button8 = ttk.Button(text = '4', command = add_4)
button8.place(x=130, y=90)

button9 = ttk.Button(text = '5', command = add_5)
button9.place(x=40, y=130)

button10 = ttk.Button(text = '6', command = add_6)
button10.place(x=70, y=130)

button11 = ttk.Button(text = '7', command = add_7)
button11.place(x=100, y=130)

button12 = ttk.Button(text = '8', command = add_8)
button12.place(x=130, y=130)

button13 = ttk.Button(text = '9', command = add_9)
button13.place(x=70, y=170)

button14 = ttk.Button(text = '0', command = add_0)
button14.place(x=100, y=170)

button15 = ttk.Button(text = 'clr', command = clear_cal)
button15.place(x=40, y=210)

button16 = ttk.Button(text = '=', command = calculate)
button16.place(x=130, y=210)

window.mainloop()