"""
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:

path – шлях до файлу.
Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:

Використовуйте менеджер контексту для читання з файлу
"""
import pickle

def get_credentials_users(path):
    credentials_list = []
    with open(path, 'rb') as file:
        for line in file:
            credentials_list.append(line.decode().strip())
    return credentials_list

file_path = './module_6/user_credentials.dat'
result = get_credentials_users(file_path)
print(result)