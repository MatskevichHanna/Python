#  Напишите программу, которая принимает на вход вещественное число 
#  и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

number = input('Введите число: ')
list_num = list(number)
semple_list = []
for i in range(0, len(list_num)):
    if list_num[i].isdigit():
        semple_list.append(int(list_num[i]))
sum_numbers = sum(semple_list)
print(number, '->', sum_numbers)