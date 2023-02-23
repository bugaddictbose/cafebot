from tkinter import *
from random import *
import time


def trprt():
    win.destroy()
    kps = "KPS"
    start = str(randint(111,199))
    mid = str(randint(10,99))
    end = str(randint(000,900))
    transacid = kps + start + end + mid
    us = "____________________\n\n"
    fwrite= "TRANSACTION SUCCESSFULL\n"+us+"\nYour TRANSACTION ID is:\n" + transacid + '\n'+us+ 'Thank you. Visit again'
    print(fwrite)
    time.sleep(10)

def payc():
    paysc = Toplevel(win)
    paysc.title("PAYMENT")
    paysc.attributes('-fullscreen',True)
    payl = Label(paysc, text="Please pay Rs.20/- to proceed.", font='70', pady=150)
    payl.pack()
    paid = Button(paysc, text='PAID!', width=30 , command=trprt)
    paid.pack()
    
def pays():
    payss = Toplevel(win)
    payss.title("PAYMENT")
    payss.attributes('-fullscreen',True)
    payl = Label(payss, text="Please pay Rs.15/- to proceed.", font='70', pady=150)
    payl.pack()
    paid = Button(payss, text='PAID!', width=30 , command=trprt)
    paid.pack()

def payb():
    paysb = Toplevel(win)
    paysb.title("PAYMENT")
    paysb.attributes('-fullscreen',True)
    payl = Label(paysb, text="Please pay Rs.30/- to proceed.", font='70', pady=150)
    payl.pack()
    paid = Button(paysb, text='PAID!', width=30, command=trprt)
    paid.pack()

def paych():
    paysch = Toplevel(win)
    paysch.title("PAYMENT")
    paysch.attributes('-fullscreen',True)
    payl = Label(paysch, text="Please pay Rs.5/- to proceed.", font='70', pady=150)
    payl.pack()
    paid = Button(paysch, text='PAID!', width=30 , command=trprt)
    paid.pack()

def dessert():
    des = Toplevel(win)
    des.title("Dessert")
    cakbut = Button(des, text="CAKE", width=20, command=payc)
    swebut = Button(des, text="SWEET", width=20, command=pays)   
    cakbut.pack()
    swebut.pack()

def snack():
    snc = Toplevel(win)
    snc.title("Snack")
    bugbut = Button(snc, text="BURGER", width=20, command=payb)
    chpbut = Button(snc, text="CHIPS", width=20, command=paych)   
    bugbut.pack()
    chpbut.pack()    
win = Tk()
win.title('KPS Canteen Bot')
win.geometry("600x300")

food = StringVar()
name = StringVar()

welcometext = Label(win, text="Welcome to ", font='arial 32')
welcometext2 = Label(win, text="KPS Canteen", font='arial 32')
#idl = Label(win, text= "May I know your name?", font='24')
#idq = Entry(win, variable = name, width=20)
passed = Label(win)
labl = Label(win, text= "PLACE ORDER", font='24')
desbut = Button(win, text="DESSERT", width=20, command=dessert)
sncbut = Button(win, text="SNACK", width=20, command=snack)

welcometext.grid(row=0, column=0)
welcometext2.grid(row=0, column=1)
#idl.grid(row=2, column=0)
#idq.grid(row=2, column=1)
passed.grid(row=3, column=0)
labl.grid(row=4, column=0, padx=10, pady=20)
desbut.grid(row=5, column=0, pady=10)
sncbut.grid(row=5, column=1, pady=10)
win.mainloop()
