""" Программа анализа предложений на гласные буквы """
vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Введите текст для анализа на гласные: ')
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for key, value in sorted(found.items()):
    print(key, 'была найдена', value, 'раз')
