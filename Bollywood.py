import tkinter
from tkinter import *
import random
from tkinter import messagebox 


answers=["Maine Pyar Kiya","Prem Ratan Dhan Payo","Kaho Na Pyar Hai","Agnipath","Anand","Koi Mil Gaya","Hungama","Sharabi"]
words=["I Loved","Love jewel finds wealth","Say there is love","Fireway","Pleasure","I found someone","Commotion","Drunkard"]

num=random.randrange(0,9,1)

def default():
     global words,answers,num
     lb1.config(text=words[num])


def res():
    global words,answers,num
    num = random.randrange(0,9, 1)
    lb1.config(text = words[num])
    e1.delete(0, END)


def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("YAYY", "You got it right")
        res()
    else:
        messagebox.showerror("AWWW", "Think again")
        e1.delete(0, END)

root=tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Bollywood")
root.configure(background="#FEC3FC")


lb1=Label(root,text="Write here ",font=("Impact",18),fg="#000000")
lb1.pack(pady=30,ipady=10,ipadx=10)

ans1=StringVar()

e1=Entry(root,font=("Verdana",16),textvariable=ans1,)
e1.pack(ipady=5,ipadx=5)

btncheck=Button(root,text="CHECK",font=("Comic sans ms",14),width=16,bg="#4C4848",fg="#6ab04c",relief=GROOVE,command=checkans)
btncheck.pack(pady=40)

btnreset=Button(root,text="PASS",font=("Comic sans ms",14),width=16,bg="#4C4848",fg="#EA425C",relief=GROOVE,command=res)
btnreset.pack()


default()

root.mainloop()
