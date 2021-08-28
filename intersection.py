# пересечение с весом

"""
Необходимо найти итоговую строку слева на право
Входной формат: [
    {
        'char': 'a', # буква
        'coords': [2, 3] # координаты x0, x1
        'scor': 100 # скоринг от 1 до 100
    }
]
Если буква пересекается (длина пересечения больше 0) с другой - должна выводиться буква с наибольшим скорингом.
"""


def some_func1(module_result):
    for i in range(len(module_result)):
        for j in range(len(module_result)):
            if module_result[i]['coords'][0] < module_result[j - 1]['coords'][0] < module_result[i]['coords'][1]:
                if module_result[i]['char'] != module_result[j - 1]['char']:
                    if module_result[i]['scor'] > module_result[j - 1]['scor']:
                        print(module_result[i]['char'], end='')
                    else:
                        print(module_result[j - 1]['char'], end='')

            elif module_result[i]['coords'][0] < module_result[j - 1]['coords'][1] < module_result[i]['coords'][1]:
                if module_result[i]['char'] != module_result[j - 1]['char']:
                    if module_result[i]['scor'] > module_result[j - 1]['scor']:
                        print(module_result[i]['char'], end='')
                    else:
                        print(module_result[j - 1]['char'], end='')


module_result = [
    {
        'char': 'a',
        'coords': [1, 3],
        'scor': 70
    },
    {
        'char': 'b',
        'coords': [5, 7],
        'scor': 80
    },
    {
        'char': 'd',
        'coords': [6, 8],
        'scor': 60
    },
    {
        'char': 'y',
        'coords': [1, 2],
        'scor': 90
    },
    {
        'char': 'z',
        'coords': [9, 10],
        'scor': 90
    }
]

some_func1(module_result=module_result)
