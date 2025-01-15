"""
Observer class for notifying suscriptors of the CalculatorInterface of changes in the value of the Calculator instance
"""
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, value):
        pass
