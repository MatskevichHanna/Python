# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def input_list():
    numbers = input('Введит несколько чисел через пробел: ').split(" ")
    return numbers

def find_sum(data_list):
    # what_find = input('Что ищем?')
    result = []
    for i in range(len(data_list)):
        if i % 2 != 0:
            result.append(i)
        return result                 # return f'Индекс нечетного элемента -> {i}'

elements = input_list()
result_list = find_sum(elements)
print(f'Элементы списка, стоящие на нечётной позиции: {result_list}')



