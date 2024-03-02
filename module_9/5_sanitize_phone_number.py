'''
У модулі 5 ми написали функцію sanitize_phone_number для нормалізації рядка з телефонним номером. 
І тут ідеально підійде створення декоратора для функції sanitize_phone_number.
Декоратор повинен додавати для коротких номерів префікс +38, а для повного міжнародного номера (з 12 символом) - тільки знак +. 
Реалізуйте декоратор format_phone_number для функції sanitize_phone_number з необхідним функціоналом.
'''
import re
def format_phone_number(func):
    def inner(phone):
        cleaned_phone = func(phone)
        return '+' + cleaned_phone if len(cleaned_phone) == 12 else '+38' + cleaned_phone
    return inner

@format_phone_number
def sanitize_phone_number(phone):
    return re.sub(r'\D', '', phone)
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", "")
#     )
#     return new_phone


print(sanitize_phone_number("   345694564564"))
print(sanitize_phone_number("(050)8889900"))