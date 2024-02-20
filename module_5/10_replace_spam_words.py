'''
У шостій задачі ми писали функцію is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті повідомлення. Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон. Наприклад, всі "погані" слова замінюватимемо зірочками. Напишіть функцію replace_spam_words, яка приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words), та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. Визначити нечутливість до регістру стоп-слів.
'''
import re

def replace_spam_words(text, spam_words):
    # # Create a case-insensitive regex pattern for all spam words
    # pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, spam_words)) + r')\b', re.IGNORECASE)

    # # Replace spam words with asterisks using a lambda function
    # replaced_text = pattern.sub(lambda match: '*' * len(match.group()), text)

    # return replaced_text
    
        
    pattern = re.compile('|'.join(spam_words), re.IGNORECASE)
    return pattern.sub(lambda match: '*' * len(match.group()), text)
    return pattern.sub(replace_with_asterisks, text)


def replace_with_asterisks(match):
    return '*' * len(match.group())

# Test case
message = "This is a bad example, don't use bad words!"

# List of prohibited words
stop_words = ["bad", "example"]

result = replace_spam_words(message, stop_words)
print(result)
