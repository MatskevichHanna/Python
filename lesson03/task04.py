# Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

from function import give_int

def int_to_binary(number: int) -> str:
    binary = []
    while number // 2 != 0:
        binary.insert(0, number % 2)
        number //= 2
    binary.insert(0, number)
    result = "".join(map(str, binary))
    return result

num = give_int('Введите натуральное число: ', 1)
binary = int_to_binary(num)
print(f'{num} => {binary}')