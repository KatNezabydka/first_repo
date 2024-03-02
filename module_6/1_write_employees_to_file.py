"""
У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:

['Robert Stivenson,28', 'Alex Denver,30']
Це список рядків із прізвищем та віком співробітника, розділеними комами.

Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з нового рядка.

Функція запису в файл write_employees_to_file(employee_list, path), де:

path – шлях до файлу.
employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
[['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
Вимоги:

запишіть вміст employee_list у файл, використовуючи режим "w".
ми поки що не використовуємо менеджер контексту with
кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:
Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
"""
def write_employees_to_file(employee_list, path):
    file = open(path, "w")
    for department in employee_list:
        for employee in department:
            file.write(employee + "\n")

    file.close()

employee_list = [['60b90c1c13067a15887e1ae1,Tayson,3', '60b90c2413067a15887e1ae2,Vika,1'], ['60b90c2e13067a15887e1ae3,Barsik,2']]
path_to_file = "./module_6/employees.txt"

write_employees_to_file(employee_list, path_to_file)
