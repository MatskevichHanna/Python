# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            if not (X or Y or Z) == (not X and not Y and not Z):
                print(f'{X} \t {Y} \t {Z} \t {not (X or Y or Z) == (not X and not Y and not Z)}')