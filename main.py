# Import the required libraries
from tkinter import *
from tkinter import ttk
from utils.calculator import Calculator
import tkinter as tk

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")
win.resizable(False, False)

calculator = Calculator()
operand_left = None
operand_right = None
operator = ''
just_added_operator = False

def set_value(value: str):
    entry.delete(0, END)  
    entry.insert(0, value)  

def update_value():
    set_value(str(calculator.value))

entry = Entry(win, font=('Arial', 14))
entry.pack(pady=10)
# entry.config(state="disabled")

def add_digit(digit):
    global just_added_operator
    if not just_added_operator:
        calculator.input_digit(digit)
    else:
        calculator.value = digit
        just_added_operator = False
    update_value()

def restart_calculator():
    calculator.restart()
    update_value()

def operate_add():
    global operand_left, operand_right, operator, just_added_operator
    if operand_left is None:        
        operator = '+'
        operand_left = calculator.value
    elif operator == '+':
       operand_right = calculator.value
       calculator.value = operand_left
       calculator.add(operand_right)
       operand_left = calculator.value
       update_value()
    else:
        operator = '+'
    just_added_operator = True    

def operate_subtract():
    global operand_left, operand_right, operator,just_added_operator
    if operand_left is None:  
        operator = '-'
        operand_left = calculator.value
    elif operator == '-':
       operand_right = calculator.value
       calculator.value = operand_left
       calculator.subtract(operand_right)
       operand_left = calculator.value
       update_value()
    else:
       operator = '-' 
    just_added_operator = True   

def operate_multiply():
    global operand_left, operand_right, operator, just_added_operator
    if operand_left is None:        
        operator = '*'
        operand_left = calculator.value
    elif operator == '*':
       operand_right = calculator.value
       calculator.value = operand_left
       calculator.multiply(operand_right)
       operand_left = calculator.value
       update_value()
    else:
        operator = '*'
    just_added_operator = True    

def operate_equal():
    global operand_left, operand_right, operator
    if operand_left is not None and operand_right is not None:
        match operator:
            case '+':
                calculator.value = operand_left
                calculator.add(operand_right)
                update_value()
            case '-':
                calculator.value = operand_left
                calculator.subtract(operand_right)
                update_value()
            case '*':
                calculator.value = operand_left
                calculator.multiply(operand_right)
                update_value()
    elif operand_left is not None and operator:
        operand_right = calculator.value
        match operator:
            case '+':
                calculator.value = operand_left
                calculator.add(operand_right)
                update_value()
            case '-':
                calculator.value = operand_left
                calculator.subtract(operand_right)
                update_value()
            case '*':
                calculator.value = operand_left
                calculator.multiply(operand_right)
                update_value()

    operand_left = calculator.value
    operand_right = None
    operator = ''


positions_buttons = [(160,190),(100,100),(130,100),(160,100),(100,130),(130,130),(160,130),(100,160),(130,160),(160,160)]   

for i in range(len(positions_buttons)):
    button_i = tk.Button(win, text= str(i))
    button_i.pack(pady=20)
    button_i.place(x=positions_buttons[i][0],y=positions_buttons[i][1],width=25,height=25)
    button_i.config(command=lambda digit=i: add_digit(digit))

ttk.Button(win, text= "CE", command=restart_calculator).pack(pady= 20)

ttk.Button(win, text= "+", command=operate_add).pack(pady= 20)

ttk.Button(win, text= "-", command=operate_subtract).pack(pady= 20)

ttk.Button(win, text= "*", command=operate_multiply).pack(pady= 20)

ttk.Button(win, text= "=", command=operate_equal).pack(pady= 20)

update_value()

win.mainloop()