"""Сообщение в виде битовой карты
Отображает текстовое сообщение в соответствии с указанной битовой картой

От оригинала отличается, тем что карта читается из файла
"""

import sys
import os

file_path = os.path.dirname(__file__)
with open(f'{file_path}/bitmapworld.txt', 'r', encoding='utf8') as file:
    bitmap = file.readlines()

print('Битовое сообщение')
print('Введите сообщение для показа на битовой карте.')
message = input('> ')
if message == '':
    sys.exit()
    
# Проходим в цикле по всем строкам битовой карты:
for line in bitmap:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Выводим пустое пространство согласно пробелу в битовой карте:
            print(' ', end='')
        else:
            # Выводим символ сообщения:
            print(message[i % len(message)], end='')
    print()
    
