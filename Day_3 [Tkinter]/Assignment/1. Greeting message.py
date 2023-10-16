import tkinter as ttk

window = ttk.Tk()
window.title("Window")
window.minsize(300, 300)

label1 = ttk.Label(text = "Hello World!", font= ("Comic Sans MS", 20))
label1.pack(anchor = "w")

window.mainloop()