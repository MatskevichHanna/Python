# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from function import give_int, random_list

def pair_mult(data_list):
    multiple = list()
    for i in range(len(data_list) // 2 + len(data_list) % 2):
        multiple.append(data_list[i] * data_list[-1 - i])
    return multiple

size = give_int('Введите длину списка: ', 1)
numbers = random_list(size)
print(numbers)
print(f'Произведение пар чисел списка = {pair_mult(numbers)}')