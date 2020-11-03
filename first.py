from tkinter import *
import tkinter
from tkinter import messagebox
import mysql.connector
from time import sleep

root = Tk()
root.title("Online Ticket Booking")
title=tkinter.Label(root,text="Online Ticket Booking",bg="#F44336",fg="white",font=("arrial",32,"bold"))
title.pack(fill=BOTH,pady=2,padx=1)
photo = PhotoImage(file = "bg.jpg")
root.geometry("1366x768+200+10")
w = Label(root, image=photo)
w.pack()

def first():
	root.quit()
	root.destroy()
	sleep(1)
	import second


B2=tkinter.Button(root,text="ONLINE\nTICKET BOOKING!",fg='white',bg='#2962FF',font=("arrial",16,"bold"),height=3,width=20,command=first)
B2.place(x=500,y=500)


src_options = ['Mumbai', "Pune", "satara"]
dest_options = ['Kolhaapur', 'Sangli']

root.mainloop()
