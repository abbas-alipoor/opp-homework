#40. Create a class WeatherApp that uses tkinter to create a weather information GUI.import tkinter as tk
from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.title("WeatherApp")
window.geometry("1100x600")
window.resizable(False,False)
window.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),weight=1)
window.rowconfigure((0,1,2,3),weight=1)



label = ttk.Label(window,text="WEATHER APP",font=("arial 40 bold"),background="#4a4a4a",foreground="white")
label.place(relx = 0.3,rely=0.1)
label1 = ttk.Label(window,text=" Province :",font=("arial 25"))
label1.grid(row=2,column=4)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=1)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=6)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=7)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=9)
entry_text=tk.StringVar(value="Searching...?   ")
entry = ttk.Entry(window,textvariable=entry_text,font='arial 20 ', background="#111111",foreground="black")
entry.grid(row=2,column =6)

button1 = ttk.Button(window,text= "    Today   : Kabul ---> Suuny * \n"
                                  
                                  "\n Tomorrow : Kabul ---> Rainy  ")
button1.grid(row=1,column =4 ,columnspan=3,sticky="nsew",padx =2,pady=2)
button2 = ttk.Button(window,text="    Today    : Bamyan ---> Sunny * \n"
                                  
                                  "\n Tomorrow : Bamyan ---> Rainy  ")
button2.grid(row=1,column =0 ,columnspan=4,sticky="nsew",padx =2,pady=2)
button3 = ttk.Button(window,text="    Today    : Herat ---> Cloudy \n"
                                  
                                  "\n Tomorrow : Herat ---> Sunny * ")
button3.grid(row=1,column =7,columnspan=4,sticky="nsew",padx =2,pady=2)
button4 = ttk.Button(window,text="       Today    : Helmand ---> Sunny * \n"
                                  
                                "\n      Tomorrow : Helmand ---> Rainy  ")
button4.grid(row=1,column =12 ,columnspan=4,sticky="nsew",padx =2,pady=2)
window.mainloop()

