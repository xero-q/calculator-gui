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