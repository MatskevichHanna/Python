# Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует этот список 
# следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков C# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

from typing import List

def cortage_list_creator(lang = None, numbers = None) -> List[tuple[int, str]]:

    '''
    Функция создает списки, переводит их в верхний регистр и объединяет
    '''

    if lang is None:
        lang = ['python', 'c#', 'java', 'c++']
    if numbers is None:
        numbers = [1, 2, 3, 4]
    lang = list(map(str.upper, lang))
    cortage = list(zip(numbers, lang))
    return cortage

def ord_summary(cort_item: str) -> int:

    '''
    Функция находит сумму элементов
    '''

    symbol_summary = 0
    for i in cort_item:
        symbol_summary += ord(i)
    return symbol_summary

def filter_data(data: List) -> tuple[List[tuple[int, str]], int]:

    '''
    Функция фильтрует список по сумме очков слова
    '''

    data = [(ord_summary(data[i][1]), data[i][1]) for i in range(1, len(data))
            if not ord_summary(data[i][1]) % data[i][0]]
    elem_ord_sum = 0
    for i in data:
        elem_ord_sum += i[0]
    return data, elem_ord_sum

data_list = cortage_list_creator()
result = filter_data(data_list)
print(f'Итоговый список большими буквами {result[0]} \n Сумма: {result[1]}')