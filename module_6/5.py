'''
Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write
'''
def sanitize_file(source, output):
     with open(source, "r") as file:
         source_content = file.read()

     prepared_content = ''.join(char for char in source_content if not char.isdigit())
   
     with open(output, "w") as output:
        output.write(prepared_content)   