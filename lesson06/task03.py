# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

from function06 import give_int

result = [(-3) ** i for i in range(give_int('Введите число: '))]
print(result)