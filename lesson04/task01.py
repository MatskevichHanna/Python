# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from function import give_int

def find_simple_multiplie(num):
   i = 2
   multiplie = []
   while i * i <= num:
       while num % i == 0:
           multiplie.append(i)
           num = num / i
       i = i + 1
   if num > 1:
       multiplie.append(num)
   return multiplie

print(find_simple_multiplie('Введите натуральное число:\n'))