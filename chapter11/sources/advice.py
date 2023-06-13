from random import choice

answers = ['Да!', 'Нет!', 'Неопределенный ответ', 'Извини, что?']

def give():
    """ Возвращает случайное сообщение """
    return choice(answers)