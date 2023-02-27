from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import time
from random import *

def data(name,star,feedback):
    #time.sleep(5)
    #root.destroy()
    pass

    
    

win = Tk()
win.title('Café Bot')
win.geometry('600x400')

uname = StringVar()
foodv = StringVar()

def entname():
    uname = nameent.get()
    if uname=="":
        showerror("NAME??", "Please enter your name to continue!")
    else:
        fram2()   

def trprt(name, food):
    win.destroy()
    root = Tk()
    root.title("SUCCESS")
    #root.geometry('200x400')
    feedback = StringVar()
    #stars = IntVar()
    def feedback():
        fd = Frame(root)
        fd.pack()
        def review(stars):
            
            data(name, stars, feedback)
            
        def one():
            s1.configure(text = u'\u2605')
            s2.configure(text = u'\u2606')
            s3.configure(text = u'\u2606')
            s4.configure(text = u'\u2606')
            s5.configure(text = u'\u2606')
            review(1)
        def two():
            s1.configure(text = u'\u2605')
            s3.configure(text = u'\u2605')
            s3.configure(text = u'\u2606')
            s4.configure(text = u'\u2606')
            s5.configure(text = u'\u2606')
            review(2)
        def three():
            s1.configure(text = u'\u2605')
            s2.configure(text = u'\u2605')
            s3.configure(text = u'\u2605')
            s4.configure(text = u'\u2606')
            s5.configure(text = u'\u2606')
            review(3)
        def four():
            s1.configure(text = u'\u2605')
            s2.configure(text = u'\u2605')
            s3.configure(text = u'\u2605')
            s4.configure(text = u'\u2605')
            s5.configure(text = u'\u2606')
            review(4)
        def five():
            s1.configure(text = u'\u2605')
            s2.configure(text = u'\u2605')
            s3.configure(text = u'\u2605')
            s4.configure(text = u'\u2605')
            s5.configure(text = u'\u2605')
            review(5)
        s1 = Button(fd, text = u'\u2606', command=one, width = 2)
        s1.grid(row=1, column=1)
        s2 = Button(fd, text = u'\u2606', command=two, width = 2)
        s2.grid(row=1, column=2)
        s3 = Button(fd, text = u'\u2606', command=three, width = 2)
        s3.grid(row=1, column=3)
        s4 = Button(fd, text = u'\u2606', command=four, width = 2)
        s4.grid(row=1, column=4)
        s5 = Button(fd, text = u'\u2606', command=five, width = 2)
        s5.grid(row=1, column=5)
    start = str(randint(111,199))
    end = str(randint(000,900))
    alpa = "QWERTYUIOPASDFGHJKLZXCVBNM"
    d = str()
    for i in range(3):
        w = randint(0,25)
        d += alpa[w]
    tr = d + start + end
    
    us = "____________________\n\n"
    fwrite= "TRANSACTION SUCCESSFULL\n"+ us +"\nYour TRANSACTION ID is:\n"
    order = "You have ordered: " + food
    gwrite = '\n'+us+ 'Thank you. Visit again'

    
    tri = Label(root, text=fwrite)
    tri.pack()
    hri = Label(root, text=tr)
    hri.pack()
    feedback()
    def feedb():
        feedback = rev.get()
        root.destroy()
    rev = Entry(root, width = 20)
    rev.pack()
    subrev = Button(root, text="Submit", command = feedb)
    subrev.pack()
    gri = Label(root, text=gwrite)
    gri.pack()
    
    
    root.mainloop()

def pcake():
    trprt(uname, 'CAKE')
def pburger():
    trprt(uname, 'BURGER')
def psweet():
    trprt(uname, 'SWEET')
def pchips():
    trprt(uname, 'CHIPS')

def pay(fooditem):
    ifood = fooditem
    payscr = Toplevel(win)
    payscr.attributes("-fullscreen", "True" )
    plabel = Label(payscr, font="roman 72")
    plabel.pack(pady=60)
    pbut = Button(payscr, text="PAID", width=25)
    pbut.pack()
    pbut1 = Button(payscr, text="QUIT",width=25, command=lambda: win.destroy())
    pbut1.pack()
    if ifood == 'cake':
        plabel.configure(text="Pay Rs.30")
        pbut.configure(command=pcake)
    elif ifood == 'sweet':
        plabel.configure(text="Pay Rs.20")
        pbut.configure(command=psweet)

    elif ifood == 'burger':
        plabel.configure(text="Pay Rs.50")
        pbut.configure(command=pburger)

    elif ifood == 'chips':
        plabel.configure(text="Pay Rs.10")
        pbut.configure(command=pchips)

def fram2():
    def dessert():
        def cake():
            foodv = "cake"
            pay('cake')           
        def sweet():
            foodv = "sweet"
            pay('sweet')            
        ck = Button(food, text="CAKE", command = cake)
        ck.grid(row=1,column=0)
        swt = Button(food,text="SWEET", command = sweet)
        swt.grid(row=1,column=1)       
    def snack():
        def burger():
            foodv = "burger"
            pay('burger')            
        def chips():
            foodv = "chips"
            pay('chips')            
        brg = Button(food, text="BURGER", command = burger)
        brg.grid(row=1,column=0)
        chp = Button(food, text="CHIPS", command = chips)
        chp.grid(row=1,column=1)        
    food = Frame(win)
    food.grid(row=1)
    dess = Button(food, text="DESSERT", width=14 , command = dessert)
    dess.grid(row=0,column=0)
    snck = Button(food, text="SNACK", width=14, command = snack)
    snck.grid(row=0,column=1)
    
wfrm = Frame(win)
wfrm.grid(row=0)

welc = Label(wfrm,text = "Welcome", font ="cactus 40 bold")
welc.pack()
entn = Label(wfrm,text = "Please enter your name to continue.", font= "cactus 20")
entn.pack()
nameent = Entry(wfrm, width=30)
nameent.pack()
conti = Button(wfrm,text = "CONTINUE", width=30, command=entname)
conti.pack()



win.mainloop()


