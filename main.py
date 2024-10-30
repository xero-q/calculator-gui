# Import the required libraries
from tkinter import *
from tkinter import ttk
from utils.calculator import Calculator

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("700x350")

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

def add_digit(digit: int):
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

    operand_left = calculator.value
    operand_right = None
    operator = ''

# Create a Button to display the message
ttk.Button(win, text= "0", command=lambda: add_digit(0)).pack(pady= 20)
ttk.Button(win, text= "1", command=lambda: add_digit(1)).pack(pady= 20)
ttk.Button(win, text= "2", command=lambda: add_digit(2)).pack(pady= 20)
ttk.Button(win, text= "3", command=lambda: add_digit(3)).pack(pady= 20)
ttk.Button(win, text= "4", command=lambda: add_digit(4)).pack(pady= 20)
ttk.Button(win, text= "5", command=lambda: add_digit(5)).pack(pady= 20)
ttk.Button(win, text= "6", command=lambda: add_digit(6)).pack(pady= 20)
ttk.Button(win, text= "7", command=lambda: add_digit(7)).pack(pady= 20)
ttk.Button(win, text= "8", command=lambda: add_digit(8)).pack(pady= 20)
ttk.Button(win, text= "9", command=lambda: add_digit(9)).pack(pady= 20)

ttk.Button(win, text= "CE", command=restart_calculator).pack(pady= 20)

ttk.Button(win, text= "+", command=operate_add).pack(pady= 20)

ttk.Button(win, text= "-", command=operate_subtract).pack(pady= 20)

ttk.Button(win, text= "=", command=operate_equal).pack(pady= 20)

update_value()

win.mainloop()