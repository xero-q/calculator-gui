# Import the required libraries
from tkinter import *
from tkinter import ttk
from utils.calculator import Calculator


# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

c1 = Calculator()
operand_left = None
operand_right = None
operator = ''

def set_value(value: str):
    entry.delete(0, END)  
    entry.insert(0, value)  

def update_value():
    set_value(str(c1.value))

# Create an Entry widget (input box)
entry = Entry(win, font=('Arial', 14))
entry.pack(pady=10)

def add_digit(digit: int):
    c1.input_digit(digit)
    update_value()

def restart_calculator():
    c1.restart()
    update_value()

def operate_add():
    global operand_left, operand_right, operator
    if operand_left is None:        
        operand_left = c1.value       
        set_value('')
        c1.restart()
        operator = '+'
    elif operator == '+':
       operand_right = c1.value
       c1.value = operand_left
       c1.add(operand_right)
       update_value()
    else:
        set_value('')
        c1.restart()
        operator = '+'    

def operate_subtract():
    global operand_left, operand_right, operator
    operator = '-'
    if operand_left is None:        
        operand_left = c1.value       
        set_value('')
        c1.restart()
        operator = '-'
    elif operator == '-':
       operand_right = c1.value
       c1.value = operand_left
       c1.subtract(operand_right)
       update_value()
    else:
        set_value('')
        c1.restart()
        operator = '-'    

def operate_equal():
    global operand_left, operand_right, operator
    if operand_left is not None and operand_right is not None:
        match operator:
            case '+':
                c1.value = operand_left
                c1.add(operand_right)
                update_value()
            case '-':
                c1.value = operand_left
                c1.subtract(operand_right)
                update_value()
    elif operand_left is not None and operator:
        operand_right = c1.value
        match operator:
            case '+':
                c1.value = operand_left
                c1.add(operand_right)
                update_value()
            case '-':
                c1.value = operand_left
                c1.subtract(operand_right)
                update_value()

    operand_left = c1.value
    operand_right = None
    operator = ''

# Create a Button to display the message
ttk.Button(win, text= "1", command=lambda: add_digit(1)).pack(pady= 20)
# Create a Button to display the message
ttk.Button(win, text= "2", command=lambda: add_digit(2)).pack(pady= 20)

ttk.Button(win, text= "CE", command=restart_calculator).pack(pady= 20)

ttk.Button(win, text= "+", command=operate_add).pack(pady= 20)

ttk.Button(win, text= "-", command=operate_subtract).pack(pady= 20)

ttk.Button(win, text= "=", command=operate_equal).pack(pady= 20)

update_value()

win.mainloop()