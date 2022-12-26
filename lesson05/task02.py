# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from function05 import give_int
from typing import List
from random import randint

def player_logic(player_name: str, turn_limitation: int = 28, num: int = 2021) -> int:
    sweet = 0
    while not 0 < sweet <= turn_limitation:
        sweet = give_int (f'{player_name}, сколько конфет вы хотите взять? \n')
        if sweet > turn_limitation:
            print(f'Вы не можете взять больше чем {turn_limitation}')
        elif sweet > num:
            print(f'Вы не можете взять больше чем {num}')
        return sweet

def bot_logic(player_name: str, turn_limitation: int = 28, num: int = 2021) -> int:
    sweet = 0
    if player_name == 'Anna':
        if num <= turn_limitation:
            sweet = num
        else:
            if num % turn_limitation > 1:
                sweet = num % turn_limitation - 1
            else:
                sweet = turn_limitation - num % turn_limitation + 1
    elif player_name == 'Andrey':
        if num <= turn_limitation:
            sweet = num
        else: 
            sweet = randint(1, 28)
    print(f'{player_name} взял {sweet} конфет!')
    return sweet

def vs_algo(player_tuple: List[tuple], number: int = 2021) -> None:
    first_turn = randint(0, 1)
    while number != 0:
        if player_tuple[first_turn][2] == 'man':
            sweet_amount = player_logic(player_name = player_tuple[first_turn][1], num = number)
        elif player_tuple[first_turn][2] == 'bot':
            sweet_amount = bot_logic(player_name = player_tuple[first_turn][1], num = number)
        number -= sweet_amount
        print(f'{number} of sweet remains! \n')
        if number <= 0:
            exit(print(f'{player_tuple[first_turn][1]} Вы победили! \n Поздравляем!'))
        else:
            if first_turn:
                first_turn = 0
            else:
                first_turn = 1

def menu_input() -> None:
    while True:
        print('Нажмите "1", если вы хотите играть с вторым игроком')
        print('Нажмите "2", если вы хотите играть с ботом')
        num = input('Какую операцию вы хотите сделать?')
        if num == '1':
            pl_list = [(0, input('Введите имя первого игрока: \n'), 'man'),
                       (1, input('Введите имя второго игрока: \n'), 'man')]
        elif num == '2':
            level = 0
            while level not in(1, 2):
                level = give_int('Выберите уровень \n'
                                 '1. Misha \n'
                                 '2. Не понимает что происходит \n', 1)
                if level > 2:
                    print(f"Давай же! Максимум 2, миннимум 1 игрок!")
            if level == 1:
                pl_list = [(0, input('Введите имя первого игрока: \n'), 'man'),
                           (1, 'Anna', 'bot')]
            else:
                pl_list = [(0, input('Введите имя первого игрока: \n'), 'man'),
                           (1, 'Andrey', 'bot')]
            vs_algo(pl_list)
        else:
            print('Неправильно введены данные, попробуйте еще раз!')

menu_input()

