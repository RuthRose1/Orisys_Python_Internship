import tkinter as ttk

def convert():
    m = text1.get()
    k = text2.get()
    if not k:
        m_d = int(m)
        distance =  m_d*1.609
        text2.insert(0, distance)
    else:
        k_d = int(k)
        distance =  k_d*0.6213
        text1.insert(0, distance)


def clear_distance():
    text1.delete(0, 'end')
    text2.delete(0, 'end')



window = ttk.Tk()
window.title('Miles to Kilometer Convertor')
window.minsize(500, 250)

label1 = ttk.Label(text = 'Distance (in miles): ')
label1.place(x= 10, y=10)

text1 = ttk.Entry()
text1.place(x=200, y = 10)

label2 = ttk.Label(text = 'Distance (in km): ')
label2.place(x= 10, y=50)
 
text2 = ttk.Entry()
text2.place(x=200, y =50)

button1 = ttk.Button(text = 'Convert', command = convert)
button1.place(x=220, y=90)

button2 = ttk.Button(text = 'Clear', command = clear_distance)
button2.place(x=160, y=90)

window.mainloop()