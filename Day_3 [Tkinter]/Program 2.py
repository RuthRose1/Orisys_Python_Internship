import tkinter as ttk

def button1_output():
    name = text1.get()
    print(name)
    
    
window = ttk.Tk()
window.title("My First GUI")
window.minsize(500,250)

text1 = ttk.Entry()
text1.pack()

button1 = ttk.Button(text = 'Submit', command = button1_output)
button1.pack()


window.mainloop()