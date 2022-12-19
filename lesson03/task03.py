# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

from function import give_int, random_list_float

def max_min_fract(data_list: list) -> float:
    max_fract = 0.0
    min_fract = 1.0
    for i in range(len(data_list)):
        fract_part = round(data_list[i] % 1, 4)
        if fract_part >= max_fract:
            max_fract = fract_part
        if fract_part <= min_fract:
            min_fract = fract_part
    print('Максимальное значение дробной части элементов:', max_fract)
    print('Минимальное значение дробной части элементов:', min_fract)
    summ = round(max_fract - min_fract, 4)
    return summ

size = give_int('Введите длину списка из вещественных чисел: ', 1)
numbers = random_list_float(size)
print(numbers)
print(f'Разница = {max_min_fract(numbers)}')