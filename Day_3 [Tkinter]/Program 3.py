import tkinter as ttk

def button1_output():
    name = text1.get()
    label2 = ttk.Label(text = name, font = ('Comic Sans MS', 15))
    label2.pack(side = 'bottom')
    
    
    
window = ttk.Tk()
window.title("Name display")
window.minsize(500,250)

label1 = ttk.Label(text = "Enter name: ")
label1.pack(anchor = 'n')

text1 = ttk.Entry()
text1.pack()

button1 = ttk.Button(text = 'Submit', command = button1_output)
button1.pack()


window.mainloop()