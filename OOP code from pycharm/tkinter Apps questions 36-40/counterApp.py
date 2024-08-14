#___________________________________________________________________________________________________
#36. Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and
#ecrement buttonds.

import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("CounterApp")
window.geometry("400x400")
window.config(bg="light blue")
window.resizable(False,False)
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=2)
window.columnconfigure(2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
total_m= 1000000
label1 =ttk.Label(window,text="Your current account equal :",font="arial 12",background="gray")
label1.grid(row=1,column=1,sticky="e")
global_var =1000000
label2 =ttk.Label(window,text= global_var ,font="arial 12",background="green")
label2.grid(row=1,column=2,sticky="w")
entry_var =tk.StringVar(value='Entry your amount...?')
def d_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var - new_m
    label2['text']= global_var

def i_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var + new_m
    label2['text']= global_var

entry1 = ttk.Entry(window, font="arial 12", width=20,textvariable=entry_var)
entry1.grid(row=2, column=1, sticky="e", rowspan=2)
button1 =ttk.Button(window, text="Decrement button", width=22,command=d_button)
button1.grid(row=2,column=2,sticky="w")
button2 =ttk.Button(window, text="Increment button", width=22,command=i_button)
button2.grid(row=3,column=2,sticky="w")

window.mainloop()