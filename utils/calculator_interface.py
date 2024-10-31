from .calculator import Calculator

"""
Class that actually connects all the pieces of the Calculator, it receives the Calculator itself and a method for updating the view when its value changes.
"""
class CalculatorInterface:
    def __init__(self, calculator: Calculator):
        self._calculator = calculator
        self._operand_left = None
        self._operand_right = None
        self._operator = ''
        self._just_added_operator = False
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._calculator.value)

    def add_digit(self, digit: int):
        if not self._just_added_operator:
            self._calculator.input_digit(digit)
        else:
            self._calculator.value = digit
        self._just_added_operator = False
        self.notify()

    def operate_add(self):
        if self._operand_left is None:        
            self._operator = '+'
            self._operand_left = self._calculator.value
        elif self._operator == '+':
            self._operand_right = self._calculator.value
            self._calculator.value = self._operand_left
            self._calculator.add(self._operand_right)
            self._operand_left = self._calculator.value
            self.notify()
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
            self.notify()
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
            self.notify()
        else:
            self._operator = '*'
        self._just_added_operator = True 

    def operate_divide(self):
        if self._operand_left is None:        
            self._operator = '/'
            self._operand_left = self._calculator.value
        elif self._operator == '/':
            self._operand_right = self._calculator.value
            self._calculator.value = self._operand_left
            self._calculator.divide(self._operand_right)
            self._operand_left = self._calculator.value
            self.notify()
        else:
            self._operator = '/'
        self._just_added_operator = True             
    
    def operate_equal(self):
        if self._operand_left is not None and self._operand_right is not None:
            match self._operator:
                case '+':
                    self._calculator.value = self._operand_left
                    self._calculator.add(self._operand_right)
                    self.notify()
                case '-':
                    self._calculator.value = self._operand_left
                    self._calculator.subtract(self._operand_right)
                    self.notify()
                case '*':
                    self._calculator.value = self._operand_left
                    self._calculator.multiply(self._operand_right)
                    self.notify()
                case '/':
                    self._calculator.value = self._operand_left
                    self._calculator.divide(self._operand_right)
                    self.notify()
        elif self._operand_left is not None and self._operator:
            self._operand_right = self._calculator.value
            match self._operator:
                case '+':
                    self._calculator.value = self._operand_left
                    self._calculator.add(self._operand_right)
                    self.notify()
                case '-':
                    self._calculator.value = self._operand_left
                    self._calculator.subtract(self._operand_right)
                    self.notify()
                case '*':
                    self._calculator.value = self._operand_left
                    self._calculator.multiply(self._operand_right)
                    self.notify()
                case '/':
                    self._calculator.value = self._operand_left
                    self._calculator.divide(self._operand_right)
                    self.notify()

        self._operand_left = self._calculator.value
        self._operand_right = None
        self._operator = ''
    
    def restart(self):
        self._calculator.restart()
        self.notify()