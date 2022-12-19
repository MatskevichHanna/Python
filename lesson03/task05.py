# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from function import give_int

def create_fibonacci(number: int) -> list:
    fibonacci = [0]
    fibonacci_1 = 0
    fibonacci_2 = 1
    negative = 1
    for i in range(1, number + 1):
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
        fibonacci.append(fibonacci_1)
        fibonacci.insert(0, negative * fibonacci_1)
        negative *= -1
    return fibonacci

number = give_int('Задайте число для списка Фибоначчи: ', 1)
print(create_fibonacci(number))