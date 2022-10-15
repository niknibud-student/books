import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main() -> None:
    """ Основная функция игры """
    print('''Bagels, дедуктивная логическая игра
Я загадываю {}-значное число с неповтояющимися цифрами.
Попробуй угадать какое это число. Вот некоторые подсказки:
Pico        Одна цифра правильная, но не на своем месте
Fermi       Одна цифра правильная и на своем месте
Bagels      Нет правильных цифр

Например, если загаданное число было 248 и ты задал 843, то
подсказка будет Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        secret_num = get_secret_num()
        print('Я загадал число')
        print('У тебя {} попытки, чтобы угадать его.'.format(MAX_GUESSES))
        
        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Попытка #{}'.format(num_guesses))
                guess = input('> ')
            
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1
            
            if guess == secret_num:
                break
            
            if num_guesses > MAX_GUESSES:
                print('Ты израсходовал все попытки')
                print('Правильный ответ был {}'.format(secret_num))
                
        print('Хочешь еще сыграть? (да или нет)')
        if not input('> ').lower().startswith('д'):
            break
        
        print('Спасибо за игру!')
        
        
def get_secret_num() -> str:
    """ Возвращает строку из NUM_DIGITS уникальных случайных цифр.

    Returns:
        str: загаданное число
    """
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
        
    return secret_num


def get_clues(guess: str, secret_num: str) -> str:
    """Возвращает строку с подсказками pico, fermi и bagels для получения
       для полученной на входе пары из догадки и загаданного числа.

    Args:
        guess (str): догадка
        secret_num (str): загаданное число

    Returns:
        str: подсказки
    """ 
    if guess == secret_num:
        return 'Ты угадал!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # Правильная цифра на правильном месте
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # Правильная цифра на неправильном месте
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
    

if __name__ == '__main__':
    main()