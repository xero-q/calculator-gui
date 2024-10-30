from tkinter import *
from tkinter import ttk
from utils.calculator import Calculator
from utils.calculator_interface import CalculatorInterface
import tkinter as tk

win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")
win.resizable(False, False)

calculator = Calculator()

def set_value(value: str):
    entry.delete(0, END)  
    entry.insert(0, value)  

def update_value():
    set_value(str(calculator.value))

entry = Entry(win, font=('Arial', 14))
entry.pack(pady=10)

calculator_gui = CalculatorInterface(calculator,update_value)

positions_buttons = [(160,190),(100,100),(130,100),(160,100),(100,130),(130,130),(160,130),(100,160),(130,160),(160,160)]   

for i in range(len(positions_buttons)):
    button_i = tk.Button(win, text= str(i))
    button_i.pack(pady=20)
    button_i.place(x=positions_buttons[i][0],y=positions_buttons[i][1],width=25,height=25)
    button_i.config(command=lambda digit=i: calculator_gui.add_digit(digit))

ttk.Button(win, text= "CE", command=calculator_gui.restart).pack(pady= 20)

ttk.Button(win, text= "+", command=calculator_gui.operate_add).pack(pady= 20)

ttk.Button(win, text= "-", command=calculator_gui.operate_subtract).pack(pady= 20)

ttk.Button(win, text= "*", command=calculator_gui.operate_multiply).pack(pady= 20)

ttk.Button(win, text= "=", command=calculator_gui.operate_equal).pack(pady= 20)

update_value()

win.mainloop()