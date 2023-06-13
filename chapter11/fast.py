from random import choice

places = ['McDonalds', 'KFC', 'Burger King', 'Taco Bell', 'Wendys', 'Arbys', 'Pizza Hut']

def pick():
    """ Возвращает случайное место 'быстрой еды'"""
    return choice(places)