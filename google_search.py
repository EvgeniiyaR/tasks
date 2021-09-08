"""

На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.

Формат входных данных:
На вход программе подаются натуральное число n — количество строк, затем сами строки в указанном количестве, затем число k, затем сами поисковые запросы.

Формат выходных данных:
Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.

Примечание. Поиск не должен быть чувствителен к регистру символов.

"""

amount_req = int(input())
list_req, list_search, result_list = [], [], []
for _ in range(amount_req):
    req = str(input())
    list_req.append(req)
amount_search = int(input())
for _ in range(amount_search):
    search = str(input())
    list_search.append(search)
for item_req in list_req:
    count = 0
    for item_search in list_search:
        if item_search.lower() in item_req.lower():
            count += 1
        if count == amount_search:
            result_list.append(item_req)
for item in result_list:
    print(item)