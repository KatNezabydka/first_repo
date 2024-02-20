'''
Напишіть функцію визначення кількості днів у конкретному місяці. 
Ваша функція повинна приймати два параметри:
    month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 
    year - рік, що складається із чотирьох цифр.
Перевірте, чи функція коректно обробляє місяць лютий високосного року.
'''
from datetime import date

def get_days_in_month(month, year):
    next_month = 1 if month == 12 else month + 1
    next_year = year + 1 if month == 12 else year
    last_day_of_month = date(next_year, next_month, 1) - date(year, month, 1)
    return last_day_of_month.days



print(get_days_in_month(12, 2024))