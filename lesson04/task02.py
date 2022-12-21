# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from typing import List

def find_original_elements(lst: list) -> list:

    '''
    Создаем новый список. 
    Находим неповторяющиеся элементы и добавляем в него.
    '''
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

lst = list(input('Введите элементы через пробел: \n').split())

try:
    list_numbers = list(map(int, lst))
    print(find_original_elements(list_numbers))
except:
    print(find_original_elements(lst))