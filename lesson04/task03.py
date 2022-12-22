# В файле, содержащем фамилии студентов и их оценки, 
# изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

from function import get_list_data
from typing import List

def create_caps_elements(lst: list, trigger_str: str) -> List[str]:
    '''
    Изменем фамилии тех студентов, которые имеют средний балл более «4» на прописные буквы.
    '''
    for i in range(len(lst)):
        if trigger_str in lst[i]:
            lst[i] = lst[i].upper()
    return lst

lst = get_list_data('C:\Users\Lenovo\Desktop\дз\lesson04\list_students_with_marks.txt', 'w', encoding= 'utf-8') as data:
for i in range(len(lst)):
    data.writelines(f'{lst[i]} \n')