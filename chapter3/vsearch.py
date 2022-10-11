""" Модуль функций поиска букв в строке """

def search_for_vowels(phrase: str) -> set:
    """ Возвращает любые гласные, найденные в полученной строке

    Args:
        phrase (str): Полученная строка

    Returns:
        set: множество найденных гласных
    """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: str='aeiou') -> set:
    """ Возвращает множество letters найденных в phrase

    Args:
        phrase (str): Полученная строка
        letters (str, optional): Набор букв которые ищем. Defaults to 'aeiou'.

    Returns:
        set: множество найденных букв
    """
    return set(letters).intersection(set(phrase))
