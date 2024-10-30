import random
import tkinter as tk
from tkinter import messagebox


# Списки для работы функции, генерирующей ключ
DOUBLE_LATIN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
DOUBLE_NUMBERS = "01234567890123456789"
SYMBOLS = "012345678ABCDEFGHIJKLMNOPQRSTUVWXYZ"
created_keys = []


def create_key(a):
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

    # Первый блок ключа
    for row in range(5):
        key_creation += random.choice(SYMBOLS)
    main_key += key_creation

    for other_blocks in range(3):

        key_creation = list(key_creation)
        key_creation.pop(random.randint(0,len(key_creation)-1))

        # Второй блок ключа
        if len(key_creation) == 4:
            for symbol in range(len(key_creation)):
                if key_creation[symbol] in DOUBLE_LATIN_ALPHABET:
                    key_creation[symbol] = DOUBLE_LATIN_ALPHABET[DOUBLE_LATIN_ALPHABET.index(key_creation[symbol])+int(a[0])]
                if key_creation[symbol] in DOUBLE_NUMBERS:
                    key_creation[symbol] = DOUBLE_NUMBERS[DOUBLE_NUMBERS.index(key_creation[symbol])+int(a[0])]

        # Третий блок ключа
        if len(key_creation) == 3:
            for symbol in range(len(key_creation)):
                if key_creation[symbol] in DOUBLE_LATIN_ALPHABET:
                    key_creation[symbol] = DOUBLE_LATIN_ALPHABET[DOUBLE_LATIN_ALPHABET.index(key_creation[symbol])-int(a[1])]
                if key_creation[symbol] in DOUBLE_NUMBERS:
                    key_creation[symbol] = DOUBLE_NUMBERS[DOUBLE_NUMBERS.index(key_creation[symbol])-int(a[1])]
        
        # Четвёртый блок ключа
        if len(key_creation) == 2:
            for symbol in range(len(key_creation)):
                if key_creation[symbol] in DOUBLE_LATIN_ALPHABET:
                    key_creation[symbol] = DOUBLE_LATIN_ALPHABET[DOUBLE_LATIN_ALPHABET.index(key_creation[symbol])+int(a[2])]
                if key_creation[symbol] in DOUBLE_NUMBERS:
                    key_creation[symbol] = DOUBLE_NUMBERS[DOUBLE_NUMBERS.index(key_creation[symbol])+int(a[2])]
        key_creation = "".join(key_creation)
        main_key += f'-{key_creation}'

    return main_key


def click():
    '''Функция выводит сгенерированный ключ доступа после нажатия кнопки'''
    number = number_entry.get()
    if len(number) != 3 or number == "000":
        tk.messagebox.showwarning('Ошибка','Это не трёхзначное число!')
        return 0
    else:
        if number.isdigit():
            key = create_key(number)
            main_key = tk.Label(
                root,
                text= key,
                font=('Arial_Black', 70),
                bg = '#00EE76',
                fg = 'white',
                highlightbackground="#282828",
                highlightthickness=3
            )
            main_key.place(x=150,y=600)
            created_keys.append(main_key)
            if len(created_keys) > 1:
                previous_key = created_keys.pop(0)
                previous_key.destroy()
        else:
            tk.messagebox.showwarning('Ошибка','Это не трёхзначное число!')
        return 0




# Запуск программы и размеры
root = tk.Tk()
root.title('Генератора ключа')
root.geometry('1300x800')


# Фон
bg_image = tk.PhotoImage(file='Crypto.png')
label_bg = tk.Label(root, image=bg_image)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# Верхняя надпись "Введите трёхзначное число"
input_number_label = tk.Label(
    root,
    text='Введите трёхзначное число ',
    font=('Arial_Black', 30),
    bg = '#00EE76',
    fg = 'black',
    highlightbackground="#282828",
    highlightthickness=3
)
input_number_label.place(x=30,y=140)

# Окно для ввода числа
number_entry = tk.Entry(root, width=5,borderwidth=7, font=('Arial_Black', 50))
number_entry.place(x=60, y=270)

# Надпись "Сгенерированный ключ"
key_creation_label = tk.Label(
    root,
    text='Сгенерированный ключ ',
    font=('Arial_Black', 30),
    bg = '#00EE76',
    fg = 'black',
    highlightbackground="#282828",
    highlightthickness=3
)
key_creation_label.place(x=30,y=450)

# Кнопка рядом с вводом числа
btn_key = tk.Button(
    root,
    text = "OK",
    borderwidth = 7,
    height=5,
    width=10,
    command=click
)
btn_key.place(x=320,y=263)
key_lable = tk.Label()

root.mainloop()
