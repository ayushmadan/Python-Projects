from tkinter import*
import random
import time
import tkinter as tk

c = Tk()
c.geometry("1600x800+0+0")
c.title("Restaurant Management System")

ftop = Frame(c,bg="orange",width = 1600,height=50)
ftop.pack(side=TOP)

f1 = Frame(c,width = 800,height=700)
f1.pack(side=LEFT)

f2 = Frame(c ,width = 300,height=700)
f2.pack(side=RIGHT)
localtime=time.asctime(time.localtime(time.time()))
lblinfo = Label(ftop, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="Black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(ftop, font=( 'aria' ,20, ),text=localtime,fg="black")
lblinfo.grid(row=1,column=0)

textin = StringVar()
operator =""

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=textin , bd=60 ,insertwidth=7 ,bg="orange",justify='right')
txtdisplay.grid(columnspan=4)

def clickbut(n):
    global operator
    operator += str(n)
    textin.set(operator)

def equals():
    global operator
    val=str(eval(operator))
    textin.set(val)

def popupbonus():
    popupbonuswindow = tk.Tk()
    popupbonuswindow.wm_title("ABOUT")
    label1 = Label(popupbonuswindow, text="This is a creation of Ayush Madan", font = ('arial', 50))
    label1.grid(row=5, column=2)

def clear():
    global operator
    operator = ""
    textin.set(operator)

def Random1():
    x = random.randint(1, 1000)
    randomRef = str(x)
    rand.set(randomRef)

def Ref():

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    c.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")


but0 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="0",bg="black",command=lambda:clickbut(0)).grid(row=4,column=0)
but1 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="1",bg="black",command=lambda:clickbut(1)).grid(row=3,column=0)
but2 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="2",bg="black",command=lambda:clickbut(2)).grid(row=2,column=0)
but3 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="3",bg="black",command=lambda:clickbut(3)).grid(row=1,column=0)
but4 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="4",bg="black",command=lambda:clickbut(4)).grid(row=3,column=1)
but5 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="5",bg="black",command=lambda:clickbut(5)).grid(row=2,column=1)
but6 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="6",bg="black",command=lambda:clickbut(6)).grid(row=1,column=1)
but7 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="7",bg="black",command=lambda:clickbut(7)).grid(row=3,column=2)
but8 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="8",bg="black",command=lambda:clickbut(8)).grid(row=2,column=2)
but9 = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="9",bg="black",command=lambda:clickbut(9)).grid(row=1,column=2)
butsub = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="-",bg="black",command=lambda:clickbut("-")).grid(row=1,column=3)
butmul = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="*",bg="black",command=lambda:clickbut("*")).grid(row=2,column=3)
butdiv = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="/",bg="black",command=lambda:clickbut("/")).grid(row=3,column=3)
butadd = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="+",bg="black",command=lambda:clickbut("+")).grid(row=4,column=3)
buteq = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="=",bg="black",command=equals).grid(row=4,column=2)
butc = Button(f2,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="C",bg="black",command=clear).grid(row=4,column=1)
butabout= Button(f1,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),width = 10,text="About",bg="black",command=popupbonus).grid(row=12,column=3)


rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()

ord= Button(ftop,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),width = 20,text="Generate Order No.",bg="black",command=Random1).grid(row=8,column=0)
lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="black",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="black",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="black",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="black",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="black",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="black",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="black",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="black",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="black",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="black",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="black",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="black",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="orange" ,justify='right')
txtTotal.grid(row=5,column=3)

lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="orange",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="black",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="orange",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="black",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="orange",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="black",command=qexit)
btnexit.grid(row=7, column=3)

c.mainloop()