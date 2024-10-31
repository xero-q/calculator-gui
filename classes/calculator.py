"""
Class for performing all the operations of a typical calculator

Raises:
    ZeroDivisionError: It is raised when trying to divide the current value by zero  
"""

from decimal import Decimal

class Calculator:
    def __init__(self, value = "0"):
        self._value = Decimal(value)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = Decimal(value)
    
    def add(self, value: int | float):
        self._value += Decimal(value)

    def subtract(self, value: int | float):
        self._value -= Decimal(value)

    def multiply(self, value: int | float):
        self._value *= Decimal(value)

    def divide(self, value: int | float):
        if value == 0:
            raise ZeroDivisionError('You can not divide by zero')
        
        self._value /= Decimal(value)

    def modulus(self, value: int | float):
        if value == 0:
            raise ZeroDivisionError('You can not divide by zero')
        
        self._value %= Decimal(value)

    def input_digit(self, digit: int):
        if self._value % 1 == 0: # Integer number
            self._value *= Decimal(10)
            self._value += Decimal(digit)
        else:
            str_value = str(self._value)
            pos_period = str_value.index('.')
            decimal_part_str = str_value[pos_period+1:]
            integer_part_str = str_value[:pos_period]
            decimal_part = Decimal(decimal_part_str)
            decimal_part *= 10
            decimal_part += digit
            self._value = Decimal(integer_part_str) + decimal_part/(10**(len(decimal_part_str) + 1))
   

    def restart(self):
        self._value = Decimal(0)        