'''
Підсписком (sublist) називають список, що є складовою більшого списку. Підсписок може містити один елемент, множину елементів або бути порожнім.

Наприклад, [1], [2], [3] та [4] є підсписками списку [1, 2, 3, 4]. Список [2, 3] також входить до складу [1, 2, 3, 4], але при цьому список [2, 4] не є підсписком [1, 2, 3, 4], оскільки у вихідному списку числа 2 і 4 не є сусідами.

Порожній список є підсписком будь-якого списку.

Напишіть функцію all_sub_lists, що повертає список, який містить всі можливі підсписки заданого.

Наприклад, якщо функції передано аргумент список [1, 2, 3], то функція має повернути наступний список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].

Функція all_sub_lists повинна повертати щонайменше один список з порожнім підсписком [[]].

'''
   
def all_sub_lists(data):
    sub_lists = [[]]
    if (len(data) == 0):
        return sub_lists
    for j in range(1, len(data)):
        for i in range(len(data) - j + 1):
            sub_lists.append(data[i:(j+i)])
    sub_lists.append(data)
    return sub_lists
 
list = [4, 6, 1, 3]
print(all_sub_lists(list))

# print(list[0:1])
# print(list[1:2])
# print(list[2:3])
# print(list[3:4])

# print(list[0:2])
# print(list[1:3])
# print(list[2:4])

# print(list[0:3])
# print(list[1:4])

# print(list[0:4])