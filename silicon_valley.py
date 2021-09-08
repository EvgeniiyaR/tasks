"""

Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

Формат входных данных:
В первой строке подаётся число nn – количество холодильников. В последующих nn строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 55 до 100100 символов.

Формат выходных данных:
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

"""

n = int(input())
some_str_list = []
good_list = ['a', 'n', 't', 'o']
for i in range(1, n + 1):
    some_str = input()
    some_str_list.append(some_str)
    new_list = []
    for char in some_str:
        if char in good_list:
            new_list.append(char)
    try:
        char_a_first_list = new_list[new_list.index('a'):]
        char_n_first_list = char_a_first_list[char_a_first_list.index('n'):]
        char_t_first_list = char_n_first_list[char_n_first_list.index('t'):]
        char_o_first_list = char_t_first_list[char_t_first_list.index('o'):]
        char_n_first_list_1 = char_o_first_list[char_o_first_list.index('n'):]
        result = ''.join([char_a_first_list[0], char_n_first_list[0], char_t_first_list[0], char_o_first_list[0],
                          char_n_first_list_1[0]])
        if result == 'anton':
            print(i, end=' ')
    except ValueError:
        pass