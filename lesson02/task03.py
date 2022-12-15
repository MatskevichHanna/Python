# Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

cnt = 0
number = int(input('Введите число: '))

rand = [random.randint(-100,100) for i in range(number)]

for i in range(number):
    if rand[i] < 0:
        rand.insert(i + 1, cnt)
if rand[-1] < 0:
    rand.append(0)

print(rand)