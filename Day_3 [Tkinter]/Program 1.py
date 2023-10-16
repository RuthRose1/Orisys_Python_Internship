import tkinter

def heading_change():
   label1.config(text = "Heading is changed")#This is for changing the label1 from My 1st GUI to this text when button is clicked


window = tkinter.Tk() #Only certain times will it come when running only this line; Reason: as there is no action so window opens and closes in the blink of an eye
window.title("My First GUI")
window.minsize(500,250) #_________.minsize(width, height); The values of width and height is in pixels
#tkinter.Label(window, text = 'My first GUI........').grid(column=0, row=0) #Label() uses keyword parameters;

label1 = tkinter.Label(text = 'My first GUI........')#Label() uses keyword parameters;
label1.pack()#grid() and pack() are layout managers; it is needed to place elements

label2 = tkinter.Label(text = 'Hi........', font = ("Times New Roman", 20))#Label() uses keyword parameters;
label2.pack(side = 'right') #side has only 4 options -> top, bottom, left, right
'''Above is a disadvantage of pack(), i.e., options.
Another 2 methods for layout managers are grid() and place()
place() - elements are placed using exact precision, i.e., using exact position of x-axis and y-axis.
          Disadvantage: it is hectic to find exact place
grid() - the window is in the form of a grid; the 1st cell -> (row = 0, column = 0); easier than pack and place
'''
label1.place(x=40, y=100)

button1 = tkinter.Button(text='Click me', command = heading_change)
'''We didn't give print_hello() as giving() will print hello!! before button is clicked in the window. Without ()
only when we click button will hello be displayed in the console'''


label3 =tkinter.Label(text = 'Hi........', font = ("Comic Sans MS", 20))
label3.config(text = 'Hello')
label3.pack()
button1.pack()

window.mainloop() #This line is needed to display the window; it keeps the window running so code will be b/w window = .... and window.mainloop()