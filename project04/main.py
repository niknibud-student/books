"""Блек-Джек, (с) Эл Свейгарт
Классическая карточная игра "21"
(пока без страхования и разбиения)
"""

import random
import sys

# Задаем значения констант
HEARTS = chr(9829)  # Символ 9829 - ''♥'.
DIAMONDS = chr(9830)  # Символ 9830 - '♦'.
SPADES = chr(9824)  # Символ 9824 - '♠'.
CLUBS = chr(9827)  # Символ 9827 - ''♣'.
BACKSIDE = 'backside'


def get_bet(max_bet: int) -> int:
    """Спрашиваем у игрока, сколько он ставит на этот раунд

    Args:
        max_bet (int): верхняя граница ставки

    Returns:
        int: размер ставки
    """
    while True:
        """ Продолжаем спрашивать, пока не введено допустимое значение """
        print(f'Какая ваша ставка? (1-{max_bet}, (Q) Выход)')
        bet = input('> ').upper().strip()
        if bet == 'QUIT' or bet == 'Q':
            print('Спасибо за игру!')
            sys.exit()
            
        if not bet.isdecimal():
            continue  # Игрок не ответил, спрашиваем снова
        
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet  # Игрок ввел допустимое значение ставки
        
        
def get_deck() -> list[tuple[str, str]|str]:
    """Возвращает список кортежей (номинал, масть) для всех 52 карт

    Returns:
        list: Список кортежей (номинал, масть)
    """
    deck = []
    
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # добавляем числовые карты
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # Добавляем фигурные карты и тузы
        
    random.shuffle(deck)
    return deck


def get_hand_value(cards: list[tuple[str, str]|str]) -> int:
    """Возвращает стоимость карт. 
    Фигурные карты стоят 10, тузы - 11 или 1 очко (функция подбирает подходящую стоимость карты)

    Args:
        cards (list): список карт, которые на руках у дилера или игрока, 
                      карта представляет собой кортеж (номинал, масть)

    Returns:
        int: очки за карты
    """
    value = 0
    number_of_aces = 0  # количество тузов
    
    # Добавляем стоимость карты - не туза:
    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
            
    # Добавляем стоимость туза:
    value += number_of_aces # Добавляем 1 за каждого туза
    for i in range(number_of_aces):
        # Если можно добавить еще 10 с перебором, добавляем:
        if value + 10 < 21:
            value += 10
            
    return value


def display_cards(cards: list[tuple[str, str]|str]) -> None:
    """Отображает все карты списка

    Args:
        cards (list[tuple[str]]): Карты списка дилера или игрока
    """
    rows = ['', '', '', '', '']  # Отображаемый в каждой строке текст
    
    for i, card in enumerate(cards):
        rows[0] += ' ___   '  # Выводим верхнюю строку карты.
        if card == BACKSIDE:
            # Выводим рубашку карты:
            rows[1] += '|## |  '
            rows[2] += '|###|  '
            rows[3] += '|_##|  '
        else:
            # Выводим лицевую сторону карты:
            rank, suit = card
            rows[1] += f'|{rank:>3}|  '
            rows[2] += f'| {suit} |  '
            rows[3] += f'|{rank:_<3}|  '
            
    # Выводим все строки на экран:
    for row in rows:
        print(row)
    

def display_hands(player_hand: list[tuple[str, str]|str], 
                  dealer_hand: list[tuple[str, str]|str], 
                  show_dealer_hand: bool) -> None:
    """Отображает карты игрока. Скрывает первую карту дилера, если show_dealer_hand = False

    Args:
        player_hand (list): карты игрока
        dealer_hand (list): карты дилера
        show_dealer_hand (bool): показывать ли первую карту дилера
    """
    print()
    
    if show_dealer_hand:
        print('ДИЛЕР:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('Диллер: ???')
        # Скрываем первую карту диллера:
        display_cards([BACKSIDE] + dealer_hand[1:])
    
    # Отображаем карты игрока:
    print('ИГРОК:', get_hand_value(player_hand))
    display_cards(player_hand)
    
    
def get_move(player_hand: list[tuple[str, str]|str], money: int) -> str:
    """Возвращаем действие пользователя:
    'H' - берет карту, 'S' - ничего не берет, ему хватит, 'D' - удваивает

    Args:
        player_hand (list[tuple[str, str] | str]): спиоок карт пользователя
        money (int): сумма, которую ставит пользователь

    Returns:
        str: действие пользователя
    """
    while True:
        # Определяем какие ходы может сделать игрок
        moves = ['(H) Ещё', '(S) Хватит']
        
        # Игрок может удвоить при первом ходе, это ясно из того, 
        # что у игрока ровно две карты
        if len(player_hand) == 2 and money > 0:
            moves.append('(D) Удвоить')
           
        # Получаем ход игрока:
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        
        if move in ('H', 'S'):
            return move  # Игрок сделал допустимый ход
        if move == 'D' and '(D) Удвоить' in moves:
            return move  # Игрок сделал допустимый ход


def main() -> None:
    print('''Игра "БлекДжек"
    
    Правила:
        Постарайтесь приблизиться как можно ближе к 21, не переходя границы.
        Короли, дамы и валеты стоят 10 очков.
        Тузы стоят 1 или 11 очков.
        Карты с 2 по 10 стоят своего номинала.
        (H) Ещё - для того, чтобы взять другую карту.
        (S) Хватит - прекратить брать карты.
        Во время вашей первой игры вы можете (D) Удвоить ставку, чтобы увеличить ее,
        но можете сделать это ровно один раз, прежде чем остановиться.
        В случае ничьей ставка возвращается игроку.
        Дилер прекращает брать карты если у него >= 17.
    ''')
    
    money = 5000
    
    while True:
        # Проверяем не закончились ли у игрока деньги
        if money <= 0:
            print('Вы разорены!')
            print('Хорошо, что ты играл не на реальные деньги.')
            print('Спасибо за игру!')
            sys.exit()
            
        # Даем игроку возможность сделать ставку на раунд:
        print('Ваши деньги:', money)
        bet = get_bet(money)
        
        # Сдаем дилеру и игроку по две карты из колоды:
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        
        # Обработка действий игрока
        print('Ставка:', bet)
        while True:  # Выполняем цикл до тех пор, пока игрок не скажет "хватит" или у него перебор
            display_hands(player_hand, dealer_hand, False)
            print()
            
            # Получаем ход игрока:
            move = get_move(player_hand, money - bet)
            
            # Обработка действий игрока:
            if move == 'D':
                # Игрок удваивает, он может увеличить ставку:
                addititonal_bet = get_bet(min(bet, (money - bet)))
                bet += addititonal_bet
                print(f'Ставка увеличена до {bet}')
                print('Ставка:', bet)
            
            if move in ('H', 'D'):
                # "Ещё" или "Удваиваю": игрок берет еще одну карту:
                new_card = deck.pop()
                rank, suit = new_card
                print(f'Вы вытащили {rank} {suit}')
                player_hand.append(new_card)
                
                if get_hand_value(player_hand) > 21:
                    # Перебор у игрока:
                    continue
                    
                
            if move in ('S', 'D'):
                # "Хватит" или "Удваиваю" - переход хода к другому игроку
                break
        
        # Обработка действий дилера:
        if get_hand_value(dealer_hand) < 21:
            while get_hand_value(dealer_hand) < 17:
                # Дилер берет еще одну карту:
                print('Дилер берет...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)
                
                if get_hand_value(dealer_hand) > 21:
                    break  # Перебор у дилера
                
                input('Нажми Enter, чтобы продлолжить...')
                print('\n\n')
        
        # Отображает итоговые карты на руках:
        display_hands(player_hand, dealer_hand, True)
        
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        
        # Проверяем, игрок выиграл, проиграл или сыграл в ничью
        if dealer_value > 21:
            print(f'Дилер банкрот! Вы выграли ${bet}!')
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('Вы проиграли!')
            money -= bet
        elif player_value > dealer_value:
            print(f'Вы выграли ${bet}!')
            money += bet
        elif player_value == dealer_value:
            print('Вы сыграли в ничью. Ваша ставка вернулась к вам.')
            
        input('Нажми Enter, чтобы продолжить...')
        print('\n\n')
        

if __name__ == '__main__':
    main()
                