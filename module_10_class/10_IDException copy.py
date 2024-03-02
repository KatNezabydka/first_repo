"""
Створіть клас IDException, який успадковуватиме клас Exception.

Також реалізуйте функцію add_id(id_list, employee_id),
яка додає до списку id_list ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.

Функція add_id буде викликати власне виключення IDException,
якщо employee_id не починається з '01', інакше employee_id буде додано до списку id_list.
"""
class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("Id must started with 01")
    id_list.append(employee_id)
    return id_list

id_list = ['0101', '0110', '0101']
try:
    new_id_list = add_id(id_list, '0110')
    print("Updated ID list:", new_id_list)
except IDException as e:
    print("Error:", e)