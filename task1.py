
import tkinter as tk
from tkinter import *
import math
win=tk.Tk()
win.geometry('500x500')

pic=PhotoImage(file='triangle.png')
picLabel=tk.Label(win,image=pic)
topLeft=tk.Entry(win,width=5,borderwidth=3)
middleRight=tk.Entry(win,width=5,borderwidth=3)
bottom=tk.Entry(win,width=5,borderwidth=3)
height=tk.Entry(win,width=5,borderwidth=3)
l1=tk.Label(win,text='Enter in the values of each and the area will be calculated')

l2=tk.Label(win,text='The area of the triangle is: ')
result=StringVar()
l3=tk.Label(win,textvariable=result)


def calculation():
    a=(topLeft.get())
    b=(middleRight.get())
    c=(bottom.get())
    h=(height.get())
    s=0
    
    if a!='' and b!='' and c!='':
        a=float(a)
        b=float(b)
        c=float(c)
        s=(a+b+c)/2

        answer=math.sqrt(s*(s-a)*(s-b)*(s-c))
        answer=round(answer,3)
        result.set(answer)
    elif (a=='' or b=='') and c!='' and h!='':
        c=float(c)
        h=float(h)
        answer=(c*h)/2
        result.set(answer)
    else : 
        answer='The area of the triangle cannot be calculated'
        result.set(answer)
calc=tk.Button(win,text='Calculate!',command=calculation)

picLabel.place(x=0,y=0)
l1.place(x=0,y=275)
height.place(x=325,y=135)
topLeft.place(x=160,y=120)
middleRight.place(x=420,y=180)
bottom.place(x=225,y=225)
calc.place(x=275,y=275)
l2.place(x=0,y=350)
l3.place(x=160,y=350)
win.mainloop()