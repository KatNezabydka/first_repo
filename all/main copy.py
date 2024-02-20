def cost_delivery(quantity, *_, discount=0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""
    return (5 + 2 * (quantity - 1)) * (1 - discount)

def amount_payment(payment):
    """
    Функція підсумовує значення платежів зі списку.

    :param payment_list: Список платежів, де додатні значення - це суми для сплати,
                        від'ємні - це переплати.
    :return: Сума платежів наприкінці місяця.
    """
    return sum(payment for payment in payment_list if payment > 0) 

def prepare_data(data):
    """
    Функція видаляє найбільше та найменше значення з переданого списку,
    сортує його в порядку зростання і повертає змінений список.

    :param data: Список числових значень.
    :return: Змінений список без найбільшого та найменшого значень, відсортований.
    """

    data.remove(max(data))
    data.remove(min(data))

    sorted_data = sorted(data)

    return sorted_data

# Приклад використання
input_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = prepare_data(input_data)
print(result)    


def lookup_key(data, value):
    return [key for key, val in data.items() if val == value]
    
# Приклад використання
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
search_value = 2

result = lookup_key(my_dict, search_value)
print(f"Ключі для значення {search_value}: {result}")