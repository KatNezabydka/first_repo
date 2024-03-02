'''
Є список contacts, елементи якого - словники контактів наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Розробіть функцію get_emails, яка отримує у параметрі список list_contacts та повертає список, який містить електронні адреси всіх контактів зі списку list_contacts.
Використовуйте функцію map.
'''
def get_emails(list_contacts):
    return list(map(lambda x: x.get('email', None), list_contacts))

print(get_emails([
    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
    },
    {
    "name": "Allen Raymond2",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(111) 914-3792",
    "favorite": False,
    },
    ]))