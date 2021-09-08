"""

Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

"""


def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 1:
        return False
    if counter > 2:
        return False
    else:
        return True


def get_next_prime(num):
    while is_prime(num) is True:
        num += 1
        if is_prime(num) is True:
            break
    while is_prime(num) is False:
        num += 1
        if is_prime(num) is True:
            break
    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))