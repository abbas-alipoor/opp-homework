#37. Create a class ToDoApp that uses tkinter to create a to-do list GUI where users can add and
#remove tasks.
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("ToDoApp")
window.geometry("700x400")
window.config(bg="orange")
window.resizable(False,False)
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=2)
window.columnconfigure(2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)

label1 =ttk.Label(window,text="Tasks : Teacher, Docter, ",font="arial 12",background="gray")
label1.grid(row=1,column=1,sticky="e")
list_task= ["Manager,","Officer,","Minister"]
label2 =ttk.Label(window,text= list_task ,font="arial 12",background="gray")
label2.grid(row=1,column=2,sticky="w")
entry_var =tk.StringVar(value='Entry your task...?')

def d_button():
    global list_task
    new_m =str( entry_var.get())
    for i in list_task:
        if i == new_m:
            list_task.remove(i)
    label2['text'] = list_task

def a_button():
    global list_task
    new_m =str( entry_var.get())
    list_task.append(new_m)
    label2['text']= list_task

entry1 = ttk.Entry(window, font="arial 12", width=20,textvariable=entry_var)
entry1.grid(row=2, column=1, sticky="e", rowspan=2)

button1 =ttk.Button(window, text="Delete button", width=22,command=d_button)
button1.grid(row=2,column=2,sticky="w")

button2 =ttk.Button(window, text="Add button", width=22,command=a_button)
button2.grid(row=3,column=2,sticky="w")

window.mainloop()