# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

print('Введите координаты первой точки через пробел: ')
num_X1, num_Y1 = map(int, input().split(' '))
print('Введите координаты второй точки через пробел: ')
num_X2, num_Y2 = map(int, input().split(' '))
distance = float(((num_X2 - num_X1)** 2 + (num_Y2 - num_Y1)** 2) ** 0.5)
print(int(distance * 100) / 100)