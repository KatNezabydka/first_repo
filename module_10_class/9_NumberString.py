"""
Створіть клас NumberString, успадкуйте його від класу UserString, 
визначте для нього метод number_count(self),
який буде рахувати кількість цифр у рядку.
"""
from collections import UserString


class NumberString(UserString):
    # number_count = lambda self: sum(1 for char in self.data if char.isdigit())
    def number_count(self):
        return sum(1 for char in self.data if char.isdigit())

    

countable = NumberString('dfgdfg 345')
print(countable.number_count())
