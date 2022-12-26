# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from function05 import give_int

def player_logic(player_name: str, turn_limitation: int = 28, num: int = 2021) -> int:
    sweet = 0
    while not 0 < sweet <= turn_limitation:
        sweet = give_int (f'{player_name}, сколько конфет вы хотите взять? \n, 1')
        if sweet > turn_limitation:
            print(f'Вы не можете взять больше чем {turn_limitation}')
        elif sweet > num:
            print(f'Вы не можете взять больше чем {num}')
        return sweet

def bot_logic(player_name: str, turn_limitation: int = 28, num: int = 2021) -> int:
    sweet = 0
    if player_name == 'Master Yoda':
        if num <= turn_limitation:
            sweet = num
        else:
            if num % turn_limitation > 1:
                sweet = num % turn_limitation - 1
            else:
                sweet = turn_limitation - num % turn_limitation + 1
    elif player_name == 'Jar Jar Binks':
        if num <= turn_limitation:
            sweet num
        else: 
            sweet randnit(1, 28)
    print(f'{player_name} взял {sweet} конфет!')
    return sweet

def vs_algo()