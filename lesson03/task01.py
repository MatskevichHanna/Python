# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from function import give_int, random_list

def find_sum(data_list):
    summ = 0
    for i in range(1, len(data_list), 2):
        summ += data_list[i]
    return summ                 

size = give_int('Введите длину списка: ',1)
numbers = random_list(size)
print(numbers)
print(f'Сумма элементов списка, стоящих на нечётной позиции: {find_sum(numbers)}')



