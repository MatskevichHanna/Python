# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
set_multiply = []
previous_multiply = 1
for i in range(1, number + 1):
    set_multiply.append((previous_multiply)*i)
    previous_multiply = previous_multiply * i
print(f'N = {number} -> {set_multiply}')