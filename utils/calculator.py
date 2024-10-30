"""
Class for performing all the operations of a typical calculator

Raises:
    ZeroDivisionError: It is raised when trying to divide the current value by zero  
"""
class Calculator:
    def __init__(self, value = 0):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def add(self, value: int | float):
        self._value += value

    def subtract(self, value: int | float):
        self._value -= value

    def multiply(self, value: int | float):
        self._value *= value

    def divide(self, value: int | float):
        if value == 0:
            raise ZeroDivisionError('You can not divide by zero')
        
        self._value /= value

    def input_digit(self, digit: int):
        if self._value >= 0:
            self._value *= 10
            self._value += digit

    def restart(self):
        self._value = 0