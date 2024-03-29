'''
Ви вже навчилися працювати з рядками глибше і тепер у вас є повний набір інструментів для обробки рядків за допомогою Python.

За допомогою функції zip, за аналогією прикладу теорії, створіть словник TRANS для транслітерації. Створюйте словник TRANS поза функцією translate

Напишіть функцію translate, яка проводить транслітерацію кириличного алфавіту на латинську.

Функція translate:

приймає на вхід рядок та повертає рядок;
проводить транслітерацію кириличних символів на латиницю;
Приклад виконання:

print(translate("Дмитро Короб"))  # Dmitro Korob
print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk
Примітка: У задачі, при створенні словника TRANS, код TRANS[ord(c.upper())] = l.title() буде вважатися неправильним, а TRANS[ord(c.upper())] = l.upper() — правильним. Це компроміс, тому що в першому випадку ми враховуємо великі літери, а в другому — правильно, якщо ім'я буде все великими літерами. Щоб не ускладнювати завдання, прийнято як у документах — все ім'я друкується великими.
'''
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
# TRANS = list(zip(CYRILLIC_SYMBOLS, TRANSLATION))
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    return name.translate(TRANS)

    
# Test cases
# print(TRANS)
print(translate("lмитро Короб"))  # Output: Dmitro Korob
print(translate("Олекса Івасюк"))  # Output: Oleksa Ivasyuk