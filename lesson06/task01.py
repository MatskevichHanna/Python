# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

from typing import List

def find_second_index(list_strings: List[str], search_word: str) -> int:

    '''
    Функция определяет позицию второго вхождения строки в списке
    '''

    list_indexes = [i for i, string in enumerate(list_strings) if search_word in string]
    print(list_indexes)
    try:
        return f'Индекс второго вхождения = {list_indexes[1]} '
    except:
        return 'Не найдено'

print(find_second_index(["qwe", "asd", "zxc", "qwe", "ertqwe"], 'qwe'))