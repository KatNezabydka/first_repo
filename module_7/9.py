'''
Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.

Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

Нумерація рядків іде від 0.

'''
def to_indexed(source_file, output_file):
     with open(source_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for index, line in enumerate(f_in):
            indexed_line = f"{index}: {line}" 
            f_out.write(indexed_line) 

# Приклад використання
source_file = 'module_7/input.txt'
output_file = 'module_7/output.txt'
to_indexed(source_file, output_file)
         
    