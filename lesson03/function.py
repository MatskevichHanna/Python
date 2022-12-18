from random import random, randint
from typing import Optional

def give_int(input_string: str, min_num: Optional[int] = None) -> int:
    while True:
        try:
            num = int(input(input_string))
            if min_num and num <= min_num:
                print(f'Type number bigger then {min_num}')
                continue
            return num
        except ValueError:
            print('That is not a natural nmber')

def random_list(list_len: int) -> list:
    data_list = list()
    for i in range(list_len):
        data_list.append(round(random() - randint(-10,10), 4))
    return data_list