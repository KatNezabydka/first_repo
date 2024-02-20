'''
Напишіть функцію get_phone_numbers_for_сountries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
'''
import re

def sanitize_phone_number(phone):
    return re.sub(r'[+\-\(\) ]', '', phone)
    # new_phone = (
    #     phone.strip()
    #     .removeprefix("+")
    #     .replace("(", "")
    #     .replace(")", "")
    #     .replace("-", "")
    #     .replace(" ", "")
    # )
    # return new_phone


def get_country_from_prefix(prefix):
    country_prefixes = {
        "81": "JP",
        "65": "SG",
        "886": "TW",
        "380": "UA",   
        }
    
    for country_prefix, country_code in country_prefixes.items():
        if prefix.startswith(country_prefix):
            return country_code

    return "UA"


def get_phone_numbers_for_countries(list_phones):
    phone_by_country = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }
    
    for phone in list_phones:
        sanitized_number = sanitize_phone_number(phone)
        country = get_country_from_prefix(sanitized_number)
        phone_by_country[country].append(sanitized_number)

    return phone_by_country

# Example usage:
phone_numbers_list = ["+818012345678", "+659876543210", "+886987654321", "+380987654321", "+123456789"]
result = get_phone_numbers_for_countries(phone_numbers_list)
print(result)

        
    
        
        
            
     