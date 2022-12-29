# Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

from random import randint as rnd

input_list = list(map(lambda x: rnd(1, 101), range(200)))
print(input_list)
cort_list = []

for index, elem in enumerate(input_list):
    if index != elem:
        to_add = index, elem
        cort_list.append(to_add)
print(cort_list)

filtered_list = list(filter(lambda x: (x[0] + x[1]) % 5 == 0, cort_list))
print(filtered_list)