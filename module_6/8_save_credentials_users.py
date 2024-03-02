"""
Дані про користувачів краще зберігати у форматі бінарних файлів. Тому вам необхідно створити функцію, яка буде записувати логін та пароль користувача у файл.

Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями в бінарний файл.

Де:

path – шлях до файлу.
users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, де ключ — логін (username) користувача, а значення — його пароль (password).
Вимоги:

Кожен рядок файлу повинен мати такий вигляд username:password. Такий формат запису використовують при Базовій аутентифікації.
Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого рядка username:password для кожного елемента словника users_info
"""
import pickle

def save_credentials_users(path, users_info):
    with open(path, 'wb') as file:
        for username, password in users_info.items():
            line = f"{username}:{password}\n"
            file.write(line.encode())


users_info = {'andy': 'uyro18890D', 'steve': 'oppjM13LL9e'}
path = './module_6/user_credentials.dat'
save_credentials_users(path, users_info)