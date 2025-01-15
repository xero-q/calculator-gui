from tkinter import *
from classes.calculator import Calculator
from classes.calculator_interface import CalculatorInterface
from classes.observer import Observer

import tkinter as tk

win= Tk()

# Set the size of the tkinter window
win.geometry("350x300")
win.resizable(False, False)

entry = Entry(win, font=('Arial', 14))

def set_value(value: str):
    entry.delete(0, END)  
    entry.insert(0, value)  

calculator = Calculator()

class GUIObserver(Observer):
    def update(self, value):
       set_value(value) 

def deny_manual_input(event):
    return "break"  # This prevents the key event from being processed

def main():
    entry.pack(pady=10)
    entry.place(x=50, y=20)

    # Bind the <Key> event to deny manual input
    entry.bind("<Key>", deny_manual_input)

    calculator_gui = CalculatorInterface(calculator)
    calculator_gui.attach(GUIObserver())

    positions_buttons = [(100, 220), (100, 180), (140, 180), (180, 180), (100, 140), (140, 140), (180, 140), (100, 100),
                     (140, 100), (180, 100)]

    for i in range(len(positions_buttons)):
        button_i = tk.Button(win, text=str(i))
        button_i.pack(pady=20)
        if i == 0:
            button_i.place(x=positions_buttons[i][0], y=positions_buttons[i][1], width=70, height=30)
        else:
            button_i.place(x=positions_buttons[i][0], y=positions_buttons[i][1], width=30, height=30)
        button_i.config(command=lambda digit=i: calculator_gui.add_digit(digit))

    button_ce = tk.Button(win, text="CE", command=calculator_gui.restart)
    button_ce.pack(pady=20)
    button_ce.place(x=180, y=220, width=30, height=30)

    button_plus = tk.Button(win, text="+", command=calculator_gui.operate_add)
    button_plus.pack(pady=20)
    button_plus.place(x=220, y=100, width=30, height=70)

    button_equal = tk.Button(win, text="=", command=calculator_gui.operate_equal)
    button_equal.pack(pady=20)
    button_equal.place(x=220, y=180, width=30, height=70)

    button_percent = tk.Button(win, text="%", command=calculator_gui.operate_modulus)
    button_percent.pack(pady=20)
    button_percent.place(x=100, y=60, width=30, height=30)

    button_divide = tk.Button(win, text="/", command=calculator_gui.operate_divide)
    button_divide.pack(pady=20)
    button_divide.place(x=140, y=60, width=30, height=30)

    button_multiply = tk.Button(win, text="*", command=calculator_gui.operate_multiply)
    button_multiply.pack(pady=20)
    button_multiply.place(x=180, y=60, width=30, height=30)

    button_subtract = tk.Button(win, text="-", command=calculator_gui.operate_subtract)
    button_subtract.pack(pady=20)
    button_subtract.place(x=220, y=60, width=30, height=30)

    calculator_gui.notify()

    win.mainloop()

if __name__=="__main__":
    main()

