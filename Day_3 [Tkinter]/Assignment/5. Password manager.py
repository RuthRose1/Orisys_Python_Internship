#File mode: x -> create

import tkinter as ttk
import csv
import os

label4 = None
label5 = None

def add_pwd():
    flag = 0
    global label4
    global label5
    u = text1.get()
    e = text2.get()
    p = text3.get()
    
    headers = ['Url', 'Email', 'Password']
    value = {'Url':u, 'Email':e, 'Password':p}
    
    '''with open('pwdmanager.csv', 'w+', newline='') as f:
        cr = csv.DictReader(f)  # Read the file to check for existing records
        chk_rec = any(all(row.get(key) == value for key, value in value.items()) for row in cr)'''

    if label5 and label5.winfo_exists():
        label5.config(text='')
        
        
        file = r'C:\Users\ANIL\Desktop\Orisys_Python_Internship\Day_3\Assignment\pwdmanager.csv'
        if os.path.exists(file):
            with open('pwdmanager.csv', 'a+', newline='') as f:
                cw = csv.DictWriter(f, fieldnames=headers)
                for i in cr:
                    if all(i.get(key) == value for key, value in chk.items()):
                        clear_textbox()
                        label4 = ttk.Label(text='Password exists')
                        label4.place(x=130, y=160)
                        flag = 1
                        break
                if flag == 0:
                    cw.writerow(value)
                    label4 = ttk.Label(text='Password is saved')
                    label4.place(x=150, y=160)
        else:
            print('K')
            with open('pwdmanager.csv', 'a+', newline='') as f:
                cw.writeheader()
                cw.writerow(value)
            label4 = ttk.Label(text='Password is saved')
            label4.place(x=150, y=160)
            
    '''else:
        label4 = ttk.Label(text='Password exists')
        label4.place(x=130, y=160)'''
    

def clear_textbox():
    text1.delete(0, 'end')
    text2.delete(0, 'end')
    text3.delete(0, 'end')
               
    
def check_info():
    global label4
    global label5
    if label4 and label4.winfo_exists():
        label4.config(text='')
    flag = 0
    u = text1.get()
    e = text2.get()
    p = text3.get()
    chk = {'Url':u, 'Email':e, 'Password':p} 
    with open('pwdmanager.csv', 'r', newline='') as f:
        cr = csv.DictReader(f)
        for i in cr:
           if all(i.get(key) == value for key, value in chk.items()):
               label5 = ttk.Label(text='Credentials exist')
               label5.place(x=130, y=160)
               flag = 1
               break;
            
    if(flag == 0):
        label5 = ttk.Label(text='Credentials does not exist')
        label5.place(x=130, y=160)
    


window = ttk.Tk()
window.title('Password Manager')
window.minsize(500, 500)

label1 = ttk.Label(text = 'Enter url: ')
label1.place(x=10, y=20)

text1 = ttk.Entry(width = 30)
text1.place(x=130, y=20)

label2 =ttk.Label(text = 'Enter email: ')
label2.place(x=10, y=50)

text2 = ttk.Entry(width = 30)
text2.place(x=130, y=50)

label3 = ttk.Label(text='Enter password: ')
label3.place(x=10, y=80)

text3 = ttk.Entry(show='*', width = 30)
text3.place(x=130, y=80)

button1 = ttk.Button(text = 'Save', command = add_pwd)
button1.place(x=130, y=120)

button2 = ttk.Button(text = 'Check', command = check_info)
button2.place(x=220, y=120)


window.mainloop()