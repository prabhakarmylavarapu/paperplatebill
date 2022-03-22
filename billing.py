from platform import release
import tkinter as tk
from tkinter import *   
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from turtle import width
import requests
from datetime import datetime
from tkinter import filedialog

def total_bill():
    #===============prices====================
    waterglass1_price=30
    waterglass2_price=50
    teaglass1_price=20
    teaglass2_price=15
    paperroll_price=50
    paperplate_price=0.80
    buffetplate1_price=1.40
    buffetplate2_price=2.10
    #===================quantity================
    waterglass1_q=waterglass1_qty.get()
    waterglass2_q=waterglass2_qty.get()
    teaglass1_q=teaglass1_qty.get()
    teaglass2_q=teaglass2_qty.get()
    paperroll_q=paperroll_qty.get()
    paperplate_q=paperplate_qty.get()
    buffetplate1_q=buffetplate1_qty.get()
    buffetplate2_q=buffetplate2_qty.get()
    #===============validation==============
    if waterglass1_var.get()==0:
        waterglass1_q=0
    elif waterglass1_var.get()==1 and waterglass1_qty.get()=="":
        messagebox.showerror("error","please fill the waterglass1 quantity")
        waterglass1_q=0
    if waterglass2_var.get()==0:
        waterglass2_q=0
    elif waterglass2_var.get()==1 and waterglass2_qty.get()=="":
        messagebox.showerror("error","please fill the waterglass2 quantity")
        waterglass2_q=0
    if teaglass1_var.get()==0:
        teaglass1_q=0
    elif teaglass1_var.get()==1 and teaglass1_qty.get()=="":
        messagebox.showerror("error","please fill the teaglass1 quantity")
        teaglass1_q=0
    if teaglass2_var.get()==0:
        teaglass2_q=0
    elif teaglass2_var.get()==1 and teaglass2_qty.get()=="":
        messagebox.showerror("error","please fill the teaglass2 quantity")
        teaglass2_q=0
    if paperroll_var.get()==0:
        paperroll_q=0
    elif paperroll_var.get()==1 and paperroll_qty.get()=="":
        messagebox.showerror("error","please fill the paperroll quantity")
        paperroll_q=0
    if paperplate_var.get()==0:
        paperplate_q=0
    elif paperplate_var.get()==1 and paperplate_qty.get()=="":
        messagebox.showerror("error","please fill the paperplate quantity")
        paperplate_q=0
    if buffetplate1_var.get()==0:
        buffetplate1_q=0
    elif buffetplate1_var.get()==1 and buffetplate1_qty.get()=="":
        messagebox.showerror("error","please fill the buffetplate1 quantity")
        buffetplate1_q=0
    if buffetplate2_var.get()==0:
        buffetplate2_q=0
    elif buffetplate2_var.get()==1 and buffetplate2_qty.get()=="":
        messagebox.showerror("error","please fill the buffetplate2 quantity")
        buffetplate2_q=0

    #=========================total=============================
    total_waterglass1_price=waterglass1_price * int(waterglass1_q)
    total_waterglass2_price=waterglass2_price * int(waterglass2_q)
    total_teaglass1_price=teaglass1_price * int(teaglass1_q)
    total_teaglass2_price=teaglass2_price * int(teaglass2_q)
    total_paperroll_price=paperroll_price * int(paperroll_q)
    total_paperplate_price=paperplate_price * int(paperplate_q)
    total_buffetplate1_price=buffetplate1_price * int(buffetplate1_q)
    total_buffetplate2_price=buffetplate2_price * int(buffetplate2_q)

    total_items_cost=total_waterglass1_price + total_waterglass2_price + total_teaglass1_price + total_teaglass2_price + total_paperroll_price + total_paperplate_price + total_buffetplate1_price + total_buffetplate2_price

    if items_cost.get() != "":
        items_cost.delete(0,"end")
        items_cost.insert("end",total_items_cost)
    else:
        items_cost.insert("end",total_items_cost)

    #======================billrecipt============================
    date =datetime.now().date()
    if bill_details.get(1.0,"end"):
        bill_details.delete(1.0,"end")
        bill_details.insert(1.0,f" Billno-{random.randint(100,1000)} \t{date}\n=============== Iteams(q)\n===============\nAmount ================== \n {'waterglass1('+str(waterglass1_q) +')' + '       ' + str(int(waterglass1_q) * waterglass1_price) + '       ' if waterglass1_var.get()==1 else ''}\n{'waterglass2('+str(waterglass2_q) +')' + '       ' + str(int(waterglass2_q) * waterglass2_price) + '       ' if waterglass2_var.get()==1 else ''}\n{'teaglass1('+str(teaglass1_q) +')' + '       ' + str(int(teaglass1_q) * teaglass1_price) + '       ' if teaglass1_var.get()==1 else ''}\n{'waterglass1('+str(teaglass2_q) +')' + '       ' + str(int(teaglass2_q) * teaglass2_price) + '       ' if teaglass2_var.get()==1 else ''}\n{'paperroll('+str(paperroll_q) +')' + '       ' + str(int(paperroll_q) * paperroll_price) + '       ' if paperroll_var.get()==1 else ''}\n{'paperplate('+str(paperplate_q) +')' + '       ' + str(int(paperplate_q) * paperplate_price) + '       ' if paperplate_var.get()==1 else ''}\n{'buffetplate1('+str(buffetplate1_q) +')' + '       ' + str(int(buffetplate1_q) * buffetplate1_price) + '       ' if buffetplate1_var.get()==1 else ''}\n{'buffetplate1('+str(buffetplate2_q) +')' + '       ' + str(int(buffetplate2_q) * buffetplate2_price) + '       ' if buffetplate2_var.get()==1 else ''}")


def save():
    root.filename= filedialog.asksavefile(mode="w",defaultextension='.txt')
    if root.filename is None:
        return
    file_save = str(bill_details.get(1.0,END))
    root.filename.write(file_save)
    root.filename.close()

def waterglass1_chk():
    if waterglass1_var.get()==1:
        waterglass1_qty['state']="normal"
        waterglass1_qty['bg']="#080808"
        waterglass1_qty['fg']="white"
    else:
        waterglass1_qty['state']="disabled"

def waterglass2_chk():
    if waterglass2_var.get()==1:
        waterglass2_qty['state']="normal"
        waterglass2_qty['bg']="#080808"
        waterglass2_qty['fg']="white"
    else:
        waterglass2_qty['state']="disabled"

def teaglass1_chk():
    if teaglass1_var.get()==1:
        teaglass1_qty['state']="normal"
        teaglass1_qty['bg']="#080808"
        teaglass1_qty['fg']="white"
    else:
        teaglass1_qty['state']="disabled"

def teaglass2_chk():
    if teaglass2_var.get()==1:
        teaglass2_qty['state']="normal"
        teaglass2_qty['bg']="#080808"
        teaglass2_qty['fg']="white"
    else:
        teaglass2_qty['state']="disabled"

def paperroll_chk():
    if paperroll_var.get()==1:
        paperroll_qty['state']="normal"
        paperroll_qty['bg']="#080808"
        paperroll_qty['fg']="white"
    else:
        paperroll_qty['state']="disabled"

def paperplate_chk():
    if paperplate_var.get()==1:
        paperplate_qty['state']="normal"
        paperplate_qty['bg']="#080808"
        paperplate_qty['fg']="white"
    else:
        paperplate_qty['state']="disabled"

def buffetplate1_chk():
    if buffetplate1_var.get()==1:
        buffetplate1_qty['state']="normal"
        buffetplate1_qty['bg']="#080808"
        buffetplate1_qty['fg']="white"
    else:
        buffetplate1_qty['state']="disabled"

def buffetplate2_chk():
    if buffetplate2_var.get()==1:
        buffetplate2_qty['state']="normal"
        buffetplate2_qty['bg']="#080808"
        buffetplate2_qty['fg']="white"
    else:
        buffetplate2_qty['state']="disabled"

#===============================================================================
def exit():
    message = messagebox.askquestion('notepad',"Do you want to exit the application")
    if message =="yes":
        root.destroy()
    else:
        "return"

 #==================================================================================
def clear():
    waterglass1_qty.delete(0,'end')
    waterglass1.deselect()
    waterglass1_qty['state']="disabled"
    waterglass2_qty.delete(0,'end')
    waterglass2.deselect()
    waterglass2_qty['state']="disabled" 
    teaglass1_qty.delete(0,'end')
    teaglass1.deselect()
    teaglass1_qty['state']="disabled"
    teaglass2_qty.delete(0,'end')
    teaglass2.deselect()
    teaglass2_qty['state']="disabled"
    paperroll_qty.delete(0,'end')
    paperroll.deselect()
    paperroll_qty['state']="disabled"
    paperplate_qty.delete(0,'end')
    paperplate.deselect()
    paperplate_qty['state']="disabled"
    buffetplate1_qty.delete(0,'end')
    buffetplate1.deselect()
    buffetplate1_qty['state']="disabled"
    buffetplate2_qty.delete(0,'end')
    buffetplate2.deselect()
    buffetplate2_qty['state']="disabled"

    items_cost.delete(0,'end')
    items_cost.delete(0,'end')
    bill_details.delete(1.0,"end")

root=tk.Tk()
root.geometry('700x500')
root.maxsize(600,390)
root.minsize(600,390)
root.title("     Satyanarayana Paper Plates    ")

frame=Frame(root,width=600,height=70,relief=RIDGE,borderwidth=5,bg='#0c0c0d')
frame.place(x=0,y=0)
l1=Label(frame,text="     Satyanarayana Paper Plates     ",font=('roboto',30,'bold'),bg='#1e12c9',fg='#e1e1e6')
l1.place(x=9,y=3)

#=========================================
frame1=Frame(root,width=450,height=300,relief=RIDGE,borderwidth=4,bg='#0c0c0d')
frame1.place(x=0,y=60)

items =LabelFrame(frame1,text="Items",width=300,height=250,borderwidth=3,bg='#635ea6')
items.place(x=2,y=2)

waterglass1_var= IntVar()
waterglass1=Checkbutton(items,text='Waterglass1',variable=waterglass1_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=waterglass1_chk)
waterglass1.place(x=2,y=2)

waterglass1_qty=Entry(items,width=10,borderwidth=4,relief=SUNKEN,state='disabled')
waterglass1_qty.place(x=130,y=2)
waterglass1_qty.insert(0,"0")

waterglass2_var= IntVar()
waterglass2=Checkbutton(items,text='Waterglass2',variable=waterglass2_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=waterglass2_chk)
waterglass2.place(x=2,y=22)

waterglass2_qty=Entry(items,width=10,borderwidth=4,relief=SUNKEN,state='disabled')
waterglass2_qty.place(x=130,y=22)

teaglass1_var= IntVar()
teaglass1=Checkbutton(items,text='teaglass1',variable=teaglass1_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=teaglass1_chk)
teaglass1.place(x=2,y=44)
teaglass1_qty=Entry(items,width=10,borderwidth=4,relief=SUNKEN,state='disabled')
teaglass1_qty.place(x=130,y=44)

teaglass2_var= IntVar()
teaglass2=Checkbutton(items,text='teaglass2',variable=teaglass2_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=teaglass2_chk)
teaglass2.place(x=2,y=66)
teaglass2_qty=Entry(items,width=10,borderwidth=4,relief=SUNKEN,state='disabled')
teaglass2_qty.place(x=130,y=66)

paperroll_var= IntVar()
paperroll=Checkbutton(items,text='papaerroll',variable=paperroll_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=paperroll_chk)
paperroll.place(x=2,y=88)
paperroll_qty=Entry(items,width=10,borderwidth=4,relief=SUNKEN,state='disabled')
paperroll_qty.place(x=130,y=88)

paperplate_var= IntVar()
paperplate=Checkbutton(items,text='paperplate',variable=paperplate_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=paperplate_chk)
paperplate.place(x=2,y=110)
paperplate_qty=Entry(items,width=10,borderwidth=4,relief=SUNKEN,state='disabled')
paperplate_qty.place(x=130,y=110)

buffetplate1_var= IntVar()
buffetplate1=Checkbutton(items,text='buffetplate1',variable=buffetplate1_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=buffetplate1_chk)
buffetplate1.place(x=2,y=132)
buffetplate1_qty=Entry(items,width=10,borderwidth=4,relief=SUNKEN,state='disabled')
buffetplate1_qty.place(x=130,y=132)

buffetplate2_var= IntVar()
buffetplate2=Checkbutton(items,text='buffetplate2',variable=buffetplate2_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=buffetplate2_chk)
buffetplate2.place(x=2,y=154)
buffetplate2_qty=Entry(items,width=10,borderwidth=4,relief=SUNKEN,state='disabled')
buffetplate2_qty.place(x=130,y=154)


frame2=Frame(root,width=400,height=90,relief=RIDGE,borderwidth=5,bg='#b56a31')
frame2.place(x=1,y=280)

cost_of_items=Label(frame2,text="Total cost of items",font=('verdana',8,'bold'),bg='#a331b5',fg='#0a080a')
cost_of_items.place(x=2,y=2)
items_cost=Entry(frame2,width=15,borderwidth=5,relief=SUNKEN)
items_cost.place(x=130,y=22)

frame3=Frame(root,width=300,height=350,relief=RIDGE,borderwidth=2,bg='#d5dedd')
frame3.place(x=300,y=70)
bill_details=ScrolledText(frame3,width=40,height=20,relief=SUNKEN,borderwidth=2,font=('courier',9,''))
bill_details.place(x=1,y=0)

total=Button(frame3,text='Total',relief=RAISED,borderwidth=3,font=('verdana',8,'bold'),bg='#349bad',fg='#0a0a0a',command=total_bill)
total.place(x=10,y=275)

save=Button(frame3,text='Save',relief=RAISED,borderwidth=3,font=('verdana',8,'bold'),bg='#349bad',fg='#0a0a0a',command=save)
save.place(x=100,y=275)

exit=Button(frame3,text='Exit',relief=RAISED,borderwidth=3,font=('verdana',8,'bold'),bg='#349bad',fg='#0a0a0a',command=exit)
exit.place(x=160,y=275)

clear=Button(frame3,text='Clear',relief=RAISED,borderwidth=3,font=('verdana',8,'bold'),bg='#349bad',fg='#0a0a0a',command=clear)
clear.place(x=200,y=275)

root.mainloop()











        






  