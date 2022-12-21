# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from function import give_int

def find_simple_multiplie(num: int) -> bool:

    '''
    Находим простые множители из натурального числа.
    Составляем из них список.
    '''
    for i in range(2, num):
        if not(num % i):
            return False
    return True

num = abs(give_int('Введите натуральное число: \n'))
list_numbers = [i for i in range(2, num + 1) if not num % i and find_simple_multiplie(i)]
print(list_numbers)