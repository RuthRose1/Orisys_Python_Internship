#Grid won't be set with only 1 element; it takes time
#Don't leave grid column empty as this will make the starting row as the no mentioned as columns b4 is empty, if you want space use padding
#Don't use place(), grid() and pack() together in one program; only one of them
import tkinter as ttk

def square():
    num = text1.get()
    n = int(num)
    sq = n**2
    label3 = ttk.Label(text = f'Square of the {n} = {sq}')
    label3.grid(row = 15, column = 1)

window = ttk.Tk()
window.title('Square of number: ')
window.minsize(500,250)

label1 = ttk.Label(text = 'Enter number: ')
label1.grid(row = 0, column = 1)

text1 = ttk.Entry()
text1.grid(row = 0, column = 4)

button1 = ttk.Button(text = 'Submit', command = square)
button1.grid(row = 7, column = 4)

window.mainloop()