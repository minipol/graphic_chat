from tkinter import *
import getpass
from ctypes import *
import socket
import threading

def click():
    res='ваш ip: {}'.format(txt.get())
    lbl.configure(text=res)

win=Tk()
win.title('чат')
win.geometry('500x500')

lbl=Label(win,text='введите ip компьютера:')
lbl.grid(column=0,row=0)

btn=Button(win,text='отправить',command=click)
btn.grid(column=2,row=0)

txt=Entry(win,width=10)
txt.grid(column=1,row=0)




win.mainloop()