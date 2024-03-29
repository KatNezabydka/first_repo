'''
Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
'''
def real_len(text):
    chars = {'\n', '\f', '\r', '\t', '\v'}

    length = 0

    for char in input_str:
        if char not in chars:
            length += 1
   
    return length