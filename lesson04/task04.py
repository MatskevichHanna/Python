# Шифр Цезаря - это способ шифрования, где каждая буква смещается 
# на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

text = '''
    С наступающим вас Рождеством,
    Пусть волшебством наполнится дом!
    Чтобы в сердце была теплота,
    И забудется вся суета.
    Чтоб желания ваши сбывались,
    А очаги теплом наполнялись!
    Светлый праздник — Рождество,
    И с ним приходит волшебство!
    '''

import string

eng_abc = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
rus_abc = 'фбвгдеёжзийклмнопрстуфхцчшщьыъэюя'

def crypt_text(text: str, key: int):
    '''
    Функция, которая записывает в файл шифрованный текст, спрашивает ключ, 
    считывает текст и дешифровывает его.
    '''
    new_text = ''
    for index, letter in enumerate(text.lower()):
        use_abc = rus_abc if letter in rus_abc else eng_abc
        letter_index = use_abc.find(letter)
        new_place = (letter_index + key) % len(rus_abc)
        if letter in rus_abc:
            new_text += use_abc[new_place]
        else:
            new_text += letter
    return new_text

crypted_text = crypt_text(text, 3)
print(crypted_text)
encrypted_text = crypt_text(crypted_text, -3)
print(encrypted_text)
