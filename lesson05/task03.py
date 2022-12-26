# Создайте программу для игры в ""Крестики-нолики"". 
# Для определения победы вам может пригодиться функция filter. 
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода

from function05 import give_int
from typing import List

def field_creator(turns_list: List):
    print(f'{turns_list[0]} {turns_list[1]} {turns_list[2]}')
    print(f'{turns_list[3]} {turns_list[4]} {turns_list[5]}')
    print(f'{turns_list[6]} {turns_list[7]} {turns_list[8]}')

def turn_maker(player: List, turn_list: List) -> None:
    pl = player[0]
    for i in range(len(turn_list) - 1):
        new_turn = 10
        while new_turn > 9 or turn_list[new_turn - 1] in ('X', '0'):
            new_turn = give_int(f'{pl[1]}, выберите цель для хода: ',1)
            if new_turn > 9 or turn_list[new_turn - 1] in ('X', '0'):
                print('Вы не можете занять это место! \n')
        if pl == player[0]:
            turn_list[new_turn - 1] = 'X'
            field_creator(turn_list)
            if i >= 4:
                win_condition(turn_list, player[0])
            pl = player[1]
        else:
            turn_list[new_turn - 1] = '0'
            field_creator(turn_list)
            if i >= 4:
                win_condition(turn_list, player[1])
            pl = player[0]

def win_condition(turns_list: List, player: List) -> None:
    if turns_list[0] == turns_list[1] == turns_list[2] \
        or turns_list[3] == turns_list[4] == turns_list[5] \
        or turns_list[6] == turns_list[7] == turns_list[8] \
        or turns_list[0] == turns_list[3] == turns_list[6] \
        or turns_list[1] == turns_list[4] == turns_list[7] \
        or turns_list[2] == turns_list[5] == turns_list[8] \
        or turns_list[0] == turns_list[4] == turns_list[8] \
        or turns_list[2] == turns_list[4] == turns_list[6]:
        return exit(print(f'Поздравляю {player[1]} выиграли!'))
    else:
        return

turn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')
players = [[1, player_1], [player_2]]
field_creator(turn)
turn_maker(players, turn)
