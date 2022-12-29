# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from function06 import give_int, random_list
from typing import List

def pair_mult(data_list: List[int]) -> List[int]:
    return[data_list[i] * data_list[-1 - i] for i in range(len(data_list) // 2 + len(data_list) % 2)]

dt_list = random_list(5)
print(dt_list)
res = pair_mult(dt_list)
print(res)