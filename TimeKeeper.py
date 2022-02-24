from tkinter import *
from datetime import datetime
from time import strftime

w=Tk()
w.geometry('740x245')
w.minsize(750,200)
w.title("SimpleClock")


time_a=datetime.today().strftime('%A')
time_b=(time_a.upper())
time_c=(time_b[0:2]) 

f1=Frame(w,width=740, height=245,bg='#1a1a1a')
f1.pack(expand=True)

def time():
    time_a=strftime('%H | %M | %S')  #%H   %M   %S
    l1.config(text=time_a)
    l1.after(1000,time)

l1=Label(f1, font=('Raleway',60),
          bg='#1a1a1a',
          foreground='#d3d3d3')

l1.place(x=275,y=35)
time()

l2=Label(f1, font=('Raleway',60),
          bg='#1a1a1a',
          foreground='#d3d3d3')
l2.config(text=time_c+"")
l2.place(x=75,y=35)

def labels():
    l3=Label(f1, font=('Raleway',8),bg='#1a1a1a',fg='#7f7f7f',text='Day')
    l3.place(x=130,y=140)

    l4=Label(f1, font=('Raleway',8),bg='#1a1a1a',fg='#7f7f7f',text='\nHr')
    l4.place(x=305,y=130)

    l5=Label(f1, font=('Raleway',8),bg='#1a1a1a',fg='#7f7f7f',text='\nMin')
    l5.place(x=445,y=130)

    l3=Label(f1, font=('Raleway',8),bg='#1a1a1a',fg='#7f7f7f',text='\nSec')
    l3.place(x=445+145+5,y=130)

labels()

w.mainloop()

