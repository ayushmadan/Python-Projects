from tkinter import *
import tkinter as tk

c = Tk()
c.title("Calculator")
clabel = Label(c, text = "CALCULATOR", font = 30)
textin = StringVar()
operator = ""
textdis = Entry(c,font=50, textvariable=textin, bd=60,insertwidth=15, bg='orange',justify = "right").grid(columnspan=4)

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
    label1 = Label(popupbonuswindow, text="This is a creation of Ayush Madan", font = 50)
    label1.grid(row=5, column=2)

def clear():
    global operator
    operator = ""
    textin.set(operator)

but0 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="0",bg="black",command=lambda:clickbut(0)).grid(row=4,column=0)
but1 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="1",bg="black",command=lambda:clickbut(1)).grid(row=3,column=0)
but2 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="2",bg="black",command=lambda:clickbut(2)).grid(row=2,column=0)
but3 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="3",bg="black",command=lambda:clickbut(3)).grid(row=1,column=0)
but4 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="4",bg="black",command=lambda:clickbut(4)).grid(row=3,column=1)
but5 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="5",bg="black",command=lambda:clickbut(5)).grid(row=2,column=1)
but6 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="6",bg="black",command=lambda:clickbut(6)).grid(row=1,column=1)
but7 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="7",bg="black",command=lambda:clickbut(7)).grid(row=3,column=2)
but8 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="8",bg="black",command=lambda:clickbut(8)).grid(row=2,column=2)
but9 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="9",bg="black",command=lambda:clickbut(9)).grid(row=1,column=2)
butsub = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="-",bg="black",command=lambda:clickbut("-")).grid(row=1,column=3)
butmul = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="*",bg="black",command=lambda:clickbut("*")).grid(row=2,column=3)
butdiv = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="/",bg="black",command=lambda:clickbut("/")).grid(row=3,column=3)
butadd = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="+",bg="black",command=lambda:clickbut("+")).grid(row=4,column=3)
buteq = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="=",bg="black",command=equals).grid(row=4,column=2)
butc = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="C",bg="black",command=clear).grid(row=4,column=1)
butabout = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="About",bg="black",command=popupbonus).grid(row=5,column=3)
butabout1 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="About",bg="black",command=popupbonus).grid(row=5,column=2)
butabout2= Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="About",bg="black",command=popupbonus).grid(row=5,column=1)
butabout3 = Button(c,padx=16,pady=16,bd=10,fg="orange",font=('arial',10,'bold'),text="About",bg="black",command=popupbonus).grid(row=5,column=0)
c.mainloop()
