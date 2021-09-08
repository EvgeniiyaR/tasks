"""

На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
Строчные буквы при этом остаются строчными, а прописные – прописными.

Формат входных данных:
На вход программе подается строка текста на английском языке.

Формат выходных данных:
Программа должна вывести зашифрованный текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.

"""

proposal = input().split()
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = ', ."!?'
new_list = []
for i in proposal:
    new_proposal = ''
    step = len(i.replace(',', '').replace('.', '').replace('!', '').replace('"', ''))
    for j in i:
        if j in symbols:
            new_proposal += j
        elif j == j.upper():
            old_index_upper_e = eng_upper_alphabet.find(j)
            new_index_upper_e = old_index_upper_e + step
            new_proposal += eng_upper_alphabet[new_index_upper_e]
        elif j == j.lower():
            old_index_lower_e = eng_lower_alphabet.find(j)
            new_index_lower_e = old_index_lower_e + step
            new_proposal += eng_lower_alphabet[new_index_lower_e]
    new_list.append(new_proposal)
print(' '.join(new_list))