# def split_list(grade):
#     """
#     Функція поділу списку на дві частини за середнім значенням.

#     :param grade: Список цілих чисел (бали студентів).
#     :return: Кортеж з двох списків: перший зі значеннями менше або рівними середньому, другий — строго більше.
#     """
#     if not grade:
#         # Порожній список введених балів
#         return [], []

#     average_score = sum(grade) / len(grade)

#     lower_equal_avg = [score for score in grade if score <= average_score]
#     greater_than_avg = [score for score in grade if score > average_score]

#     return (lower_equal_avg, greater_than_avg)

# # Приклад використання
# students_scores = [70, 85, 60, 45, 90, 75]
# result = split_list(students_scores)
# print(f"Список менше або рівний середньому: {result[0]}")
# print(f"Список строго більше середнього: {result[1]}")



# def game(list_of_lists, power):
#     """
#     Функція реалізації ігрового алгоритму.

#     :param list_of_lists: Список, що складається зі списків числових значень енергії.
#     :param power: Початкове значення енергії гравця.
#     :return: Загальна отримана енергія гравця.
#     """
#     for sublist in list_of_lists:
#         for energy_value in sublist:
#             if energy_value <= power:
#                 power += energy_value
#             else:
#                 break

#     return power

# # Приклад використання
# example_list = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
# initial_power = 1

# result_energy = game(example_list, initial_power)
# print(f"Загальна отримана енергія гравця: {result_energy}")

# def is_valid_pin_codes(pin_codes):
#     """
#     Функція перевірки валідності списку пін-кодів.

#     :param pin_codes: Список пін-кодів (рядків з чотирьох цифр).
#     :return: Логічне значення True, якщо список валідний, або False в іншому випадку.
#     """
#     if not pin_codes:
#         # Порожній список
#         return False

#     seen_pins = set()

#     for pin in pin_codes:
#         if not (len(pin) == 4 and pin.isdigit()):
#             # Неправильна довжина або містить не тільки цифри
#             return False

#         if pin in seen_pins:
#             # Дублікати
#             return False

#         seen_pins.add(pin)

#     return True

# # Приклад використання
# example_pin_codes = ['1103', '9034', '0011']
# result = is_valid_pin_codes(example_pin_codes)
# print(f"Чи валідний список пін-кодів: {result}")

# def is_valid_pin_codes(pin_codes):
#     if not pin_codes:
#         return False

#     exist_pins = set()

#     for pin in pin_codes:
#         if not (len(pin) == 4 and pin.isdigit()):
#             # Неправильна довжина або містить не тільки цифри
#             return False

#         if pin in exist_pins:
#             return False

#         exist_pins.add(pin)

#     return True


# def is_valid_password(password):
#     if not password or len(password) < 8:
#         return False
    
#     has_upper = any(char.isupper() for char in password)
#     has_lower = any(char.islower() for char in password)
#     has_digit = any(char.isdigit() for char in password)

#     return has_upper and has_lower and has_digit

#     return True
    

from pathlib import Path

def parse_folder(path):
    """
    Функція для аналізу вмісту директорії та розподілу файлів і піддиректорій.

    :param path: Об'єкт Path, представляючий шлях до директорії.
    :return: Кортеж із двох списків — список файлів та список директорій у директорії path.
    """
    if not path.is_dir():
        raise ValueError("Параметр 'path' повинен бути об'єктом Path, який представляє директорію.")

    files = []
    directories = []

    for entry in path.iterdir():
        if entry.is_file():
            files.append(entry.name)
        elif entry.is_dir():
            directories.append(entry.name)

    return files, directories

# Приклад використання
folder_path = Path("/Users/kornyshevaekaterina/Documents/GoIt/Projects/first_repo")
result = parse_folder(folder_path)
print("Список файлів:", result[0])
print("Список директорій:", result[1])
    
    
    
        
        
    
    
  