"""

На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

Формат входных данных:
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных:
Программа должна вывести указанный вложенный список.

"""

a = input().split(' ')
new_list, other_list = [], []
for x in a:
    if not other_list:
        other_list.append(x)
    else:
        if other_list[-1] == x:
            other_list.append(x)
        else:
            new_list.append(other_list)
            other_list = []
            other_list.append(x)
if other_list:
    new_list.append(other_list)
print(new_list)