"""

На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

Формат входных данных:
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.

Формат выходных данных:
Программа должна вывести указанный вложенный список.

"""

a = input().split(' ')
b = int(input())
new_list = []
other_list = []
for x in a:
    if not other_list:
        other_list.append(x)
        if len(other_list) == b:
            new_list.append(other_list)
            other_list = []
    else:
        if len(other_list) != b:
            other_list.append(x)
            if len(other_list) == b:
                new_list.append(other_list)
                other_list = []
if other_list:
    new_list.append(other_list)
print(new_list)