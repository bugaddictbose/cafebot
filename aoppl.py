from tkinter import *
from tkinter.ttk import *
import time
from random import *

win = Tk()
win.title('Café Bot')
win.geometry('600x400')

foodv = StringVar()

def 
def fram2():
    def dessert():
        def cake():
            foodv = "cake"
            pay(cake)
        def sweet():
            foodv = "sweet"
            pay(sweet)
        ck = Button(food, command = cake)
        ck.grid(row=1,column=0)
        swt = Button(food,command = sweet)
        swt.grid(row=1,column=1)
    food = Frame(win)
    food.grid(row=1)
    dess = Button(food, command = dessert)
    dess.grid(row=0,column=0)
    snck = Button(food, command = snack)
    snck.grid(row=0,column=1)
def entname():
    uname = nameent.get()
    fram2()
wfrm = Frame(win)
wfrm.grid(row=0)

welc = Label(wfrm,text = "Welcome")
welc.pack()
entn = Label(wfrm,text = "Please enter your name to continue.")
uname = StringVar()
nameent = Entry(wfrm)
conti = Button(wfrm,text = "continue", command=entname)


