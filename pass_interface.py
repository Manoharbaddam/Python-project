from tkinter import *
from tkinter import messagebox
import string 
import random

root =Tk()

symbols= "_@#$.*&"

def generate_password():

    try:
        alps = no_alp.get()
        ints = no_int.get()
        syms = no_sym.get()

        c = string.ascii_letters
        random_c = ''.join(random.choices(c,k=int(alps)))
        nums = string.digits
        sym = symbols
        nums_syms = nums
        random_nums = ''.join(random.choices(nums,k = int(ints)))
        random_sym = ''.join(random.choices(sym,k=int(syms)))

        password = random_c + random_nums + random_sym
        messagebox.showinfo("Generated Password Succesfully", f"Your Password is : {password}")

    except ValueError:
        messagebox.showerror("Error","Please Enter valid inputs" )

def welcome():
    title_frame = Frame(root,pady=20,padx=20,borderwidth=1,relief="solid",bg="#778da9")
    title_frame.pack(pady=20,padx=20)
    font1 = ("Times New Roman",18)
    head = Label(title_frame,text="WELCOME TO PASSWORD GENERATOR",font=font1,bg="#778da9")
    head.pack()

def Labels(use):
    font2 = ("Arial" , 12)
    entry1 = Label(text=f"How many {use} you want in password : ",font= font2,relief="flat")
    entry1.pack()

def Buttons():
    new_button = Button(text="Generate Password",command= generate_password,font=15,relief="sunken",bg="#1d3557",fg="white")
    new_button.pack(pady=10)

no_alp = StringVar()
no_int = StringVar()
no_sym = StringVar()


welcome()
Labels("letters")
no_entries = Entry(root,width=5,textvariable=no_alp) 
no_entries.pack(pady=10)

Labels("numbers")
no_entries = Entry(root,width=5,textvariable=no_int) 
no_entries.pack(pady=10)


Labels("symbols")
no_entries = Entry(root,width=5,textvariable=no_sym) 
no_entries.pack(pady=10)

Buttons()
root.bind('<Return>',lambda event=None:generate_password())
root.mainloop()