#39. Create a class LoginApp that uses tkinter to create a login form GUI.
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("loginApp")
window.geometry("400x400")
window.config(bg="light blue")
window.resizable(False,False)
window.columnconfigure(1,weight=2)
window.columnconfigure( 2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)


label1 =ttk.Label(window,text="User Name :",font="arial 20",background="light blue")
label1.grid(row=1,column=1,sticky="e")
entry_text=tk.StringVar()
entry1 = ttk.Entry(window,font="arial 12",width=15,textvariable=entry_text)
entry1.grid(row=1,column=2,sticky="w")
label2 =ttk.Label(window,text=" PassWord :",font="arial 20",background="light blue")
label2.grid(row=2,column=1,sticky="e")
entry_text1=tk.StringVar()
entry2 = ttk.Entry(window,font="arial 12",width=15,textvariable=entry_text1)
entry2.grid(row=2,column=2,sticky="w")
button =ttk.Button(window,text="Click For login",width=30)
button.place(relx=0.2,rely=0.5)

window.mainloop()







