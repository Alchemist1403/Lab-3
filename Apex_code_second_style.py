import random
import time
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from pygame import mixer


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
    if len(number) != 3 or number[0] == "0":
        tk.messagebox.showwarning('Error','Incorrect number')
        return 0
    else:
        if number.isdigit():
            create_progressbar()
            main_key = create_key(number)
            main_key = tk.Label(
                root,
                text= main_key,
                font=('Arial_Black', 50),
                bg = '#1C1C1C',
                fg = '#00C957',
                highlightbackground="#555555",
                highlightthickness=6,
                width=20
            )
            main_key.place(x=70,y=540)
            created_keys.append(main_key)
            if len(created_keys) > 1:
                previous_key = created_keys.pop(0)
                previous_key.destroy()
        else:
            tk.messagebox.showwarning('Ошибка','Это не трёхзначное число!')
        return 0

def create_progressbar():
    '''Функция создаёт анимацию загрузки'''
    generating_label = tk.Label(
        root,
        text= "Generating new key...",
        font=('Arial_Black', 20),
        bg = 'black',
        fg = '#00C957',
        width=20
    )
    generating_label.place(x=340,y=650)
    prog_bar=Progressbar(root,orient='horizontal',length=400,mode='determinate')
    prog_bar.place(x=290,y=700)
    for row in range(100):
        prog_bar['value']=row
        root.update_idletasks()
        time.sleep(0.01)
    prog_bar.destroy()
    generating_label.destroy()

# Запуск программы и размеры
root = tk.Tk()
root.title('Keygen')
root.geometry('1000x800')

# Фон
bg_image = tk.PhotoImage(file='Crypto_logo.png')
label_bg = tk.Label(root, image=bg_image)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# Верхняя надпись "Введите трёхзначное число"

input_number_label = tk.Label(
    root,
    text='Enter a three digit number: ',
    font=('Arial_Black', 30),
    bg = '#1C1C1C',
    fg = '#00C957',
    highlightbackground="#555555",
    highlightthickness=6)
root.after(5,input_number_label)
input_number_label.place(x=20,y=140)

# Окно для ввода числа
number_entry = tk.Entry(
    root,
    width=5,
    bg = '#1C1C1C',
    borderwidth=7, 
    font=('Arial_Black', 50),
    fg = '#00C957'
)
number_entry.place(x=60, y=270)

# Надпись "Сгенерированный ключ"
key_creation_label = tk.Label(
    root,
    text='Generated key: ',
    font=('Arial_Black', 30),
    bg = '#1C1C1C',
    fg = '#00C957',
    highlightbackground="#555555",
    highlightthickness=6
)
key_creation_label.place(x=30,y=450)

# Кнопка рядом с вводом числа
btn_key = tk.Button(
    root,
    text = "OK",
    borderwidth = 7,
    height=5,
    width = 10,
    activebackground = "#1C1C1C",
    bg = "#1C1C1C",
    fg = "#00C957",
    command=click
)
btn_key.place(x=300,y=267)

# Воспроизведение музыки
mixer.init()
mixer.music.load("Apex.mp3")
mixer.music.play(999)

root.mainloop()
