# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

quarter_number = int(input('Введите номер четверти:\n'))
if quarter_number == 1:
    print('X∈(0, ∞) u Y∈(0,∞)')
elif quarter_number == 2:
    print('X∈(∞, 0) u Y∈(0,∞)')
elif quarter_number == 3:
    print('X∈(∞, 0) u Y∈(∞, 0)')
elif quarter_number == 4:
    print('X∈(0, ∞) u Y∈(∞, 0)')
else:
    print('Введите число от 1 до 4: ')