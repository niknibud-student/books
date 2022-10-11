def search_for_vowels(phrase: str) -> set:
    """ Return the rest of vowels found in 'phrase'."""
    return set('aeiou').intersection(set(phrase))


def search_for_letters(phrase: str, letters: str='aieou') -> set:
    """ Returns the set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))