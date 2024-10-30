from .calculator import Calculator

"""
Class that actually connects all the pieces of the Calculator, it receives the Calculator itself and a method for updating the view when its value changes.
"""
class CalculatorInterface:
    def __init__(self, calculator: Calculator, update_method):
        self._calculator = calculator
        self._update_method = update_method
        self._operand_left = None
        self._operand_right = None
        self._operator = ''
        self._just_added_operator = False

    def add_digit(self, digit: int):
        if not self._just_added_operator:
            self._calculator.input_digit(digit)
        else:
            self._calculator.value = digit
        self._just_added_operator = False
        self._update_method()

    def operate_add(self):
        if self._operand_left is None:        
            self._operator = '+'
            self._operand_left = self._calculator.value
        elif self._operator == '+':
            self._operand_right = self._calculator.value
            self._calculator.value = self._operand_left
            self._calculator.add(self._operand_right)
            self._operand_left = self._calculator.value
            self._update_method()
        else:
            self._operator = '+'
        self._just_added_operator = True  

    def operate_subtract(self):
        if self._operand_left is None:        
            self._operator = '-'
            self._operand_left = self._calculator.value
        elif self._operator == '-':
            self._operand_right = self._calculator.value
            self._calculator.value = self._operand_left
            self._calculator.subtract(self._operand_right)
            self._operand_left = self._calculator.value
            self._update_method()
        else:
            self._operator = '-'
        self._just_added_operator = True 

    def operate_multiply(self):
        if self._operand_left is None:        
            self._operator = '*'
            self._operand_left = self._calculator.value
        elif self._operator == '*':
            self._operand_right = self._calculator.value
            self._calculator.value = self._operand_left
            self._calculator.multiply(self._operand_right)
            self._operand_left = self._calculator.value
            self._update_method()
        else:
            self._operator = '*'
        self._just_added_operator = True       
    
    def operate_equal(self):
        if self._operand_left is not None and self._operand_right is not None:
            match self._operator:
                case '+':
                    self._calculator.value = self._operand_left
                    self._calculator.add(self._operand_right)
                    self._update_method()
                case '-':
                    self._calculator.value = self._operand_left
                    self._calculator.subtract(self._operand_right)
                    self._update_method()
                case '*':
                    self._calculator.value = self._operand_left
                    self._calculator.multiply(self._operand_right)
                    self._update_method()
        elif self._operand_left is not None and self._operator:
            self._operand_right = self._calculator.value
            match self._operator:
                case '+':
                    self._calculator.value = self._operand_left
                    self._calculator.add(self._operand_right)
                    self._update_method()
                case '-':
                    self._calculator.value = self._operand_left
                    self._calculator.subtract(self._operand_right)
                    self._update_method()
                case '*':
                    self._calculator.value = self._operand_left
                    self._calculator.multiply(self._operand_right)
                    self._update_method()

        self._operand_left = self._calculator.value
        self._operand_right = None
        self._operator = ''
    
    def restart(self):
        self._calculator.restart()