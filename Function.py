import random


DOUBLE_LATIN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
DOUBLE_NUMBERS = "01234567890123456789"
SYMBOLS = "012345678ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def create_key(a,b,c):
    ''' Функция генерирует ключ из 4 блоков. 
        Каждый следующий блок уменьшается на один элемент.
        Первый блок состоит из 5 символов: латинских букв или цифр от 0 до 9
        Второй - из 4 символов предыдущего блока, сдвинутых на значение аргумента а вправо
        Третий - из 3 символов предыдущего блока, сдвинутых на значение аргумента b влево
        Четвёртый - из 2 символов предыдущего блока, сдвинутых на значение аргумента с вправо
        Сдвиг символа - замена его на элемент с большим или меньшим индексом 
        из списков DOUBLE_LATIN_ALPHABET и DOUBLE_NUMBERS 
    '''

    main_key = ""
    key_creation = ""

    for row in range(5):
        key_creation += random.choice(SYMBOLS)  # Первый блок ключа
    main_key += key_creation

    for other_blocks in range(3):

        key_creation = list(key_creation)
        key_creation.pop(random.randint(0,len(key_creation)-1))

        if len(key_creation) == 4:
            for symbol in range(len(key_creation)):
                if key_creation[symbol] in DOUBLE_LATIN_ALPHABET:
                    key_creation[symbol] = DOUBLE_LATIN_ALPHABET[DOUBLE_LATIN_ALPHABET.index(key_creation[symbol])+a]
                if key_creation[symbol] in DOUBLE_NUMBERS:
                    key_creation[symbol] = DOUBLE_NUMBERS[DOUBLE_NUMBERS.index(key_creation[symbol])+a] # Второй блок ключа

        if len(key_creation) == 3:
            for symbol in range(len(key_creation)):
                if key_creation[symbol] in DOUBLE_LATIN_ALPHABET:
                    key_creation[symbol] = DOUBLE_LATIN_ALPHABET[DOUBLE_LATIN_ALPHABET.index(key_creation[symbol])-b]
                if key_creation[symbol] in DOUBLE_NUMBERS:
                    key_creation[symbol] = DOUBLE_NUMBERS[DOUBLE_NUMBERS.index(key_creation[symbol])-b] # Третий блок ключа

        if len(key_creation) == 2:
            for symbol in range(len(key_creation)):
                if key_creation[symbol] in DOUBLE_LATIN_ALPHABET:
                    key_creation[symbol] = DOUBLE_LATIN_ALPHABET[DOUBLE_LATIN_ALPHABET.index(key_creation[symbol])+c]
                if key_creation[symbol] in DOUBLE_NUMBERS:
                    key_creation[symbol] = DOUBLE_NUMBERS[DOUBLE_NUMBERS.index(key_creation[symbol])+c] # Четвёртый блок ключа

        key_creation = "".join(key_creation)
        main_key += f'-{key_creation}'

    return main_key


print(create_key(1,0,0))
