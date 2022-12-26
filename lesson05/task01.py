# Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

def delete_string(input_string: str) -> str:

    '''
    Функция удаляет из текста все слова, содержащие заданную строку
    '''

    delete = input('Какую строку вы хотите удалить? \n')
    result_list = [i for i in input_string.split() if delete not in i]
    return ' '.join(result_list)

result = delete_string(input('Введите текст: \n'))
print(result)