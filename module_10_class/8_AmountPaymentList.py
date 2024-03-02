"""
Перепишемо завдання розрахунку заборгованостей з комунальних послуг за допомогою класу UserList.

payment = [1, -3, 4]


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum
Нагадаємо умову. У нас є список показань заборгованостей з комунальних послуг наприкінці місяця, список payment. Заборгованості можуть бути від'ємними — у нас переплата, або додатними, якщо потрібно сплатити за рахунками.

Створіть клас AmountPaymentList, успадковуйте його від класу UserList. Зробіть функцію amount_payment методом класу AmountPaymentList.
"""
from collections import UserList


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum

class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum(map(lambda x: int(x) if x > 0 else 0, self.data))
    


payment = [1, -3, 4]
print(amount_payment(payment))

countable = AmountPaymentList([1, -3, 4])
print(countable.amount_payment())
