"""
Имитационное моделирование парадокса дней рождения
"""

import datetime
import random
from datetime import date
from typing import List


def get_birthdays(number_of_bithdays: int) -> List[date]:
    """Возвращаем список объектов дат для случайных дней рождений

    Args:
        number_of_bithdays (ште): количество дней рождений

    Returns:
        List: список дней рождений
    """
    
    birthdays = []
    
    for i in range(number_of_bithdays):
        # Год роли не играет, главное чтобы в датах он был одинаковым
        start_of_year = datetime.date(2022, 1, 1)
        # Получаем случайны день года
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
                
    return birthdays


def get_match(birthdays: List[date]) -> None | date:
    """Возвращает объект даты рождения, встречающегося несколько раз в списке дней рождения

    Args:
        birthdays (List[date]): Список дней рождения

    Returns:
        None | List[date]: Списко повторяющихся дней рождения
    """
    
    if len(birthdays) == len(set(birthdays)):
        return None  # Все дни рождения различны
    
    # Сравниваем все дни рождения друг с другом попарно
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a+1:]):
            if birthday_a == birthday_b:
                return birthday_a  # Возвращаем найденные соответствия
            

def main() -> None:
    # Отображаем вводную информацию:
    print('''Парадокс дней рождения

Парадокс дней рождения показывает нам, что в группе из N человек вероятность того, 
что у двоих из них совпадут дни рождения, на удивление велика.
Эта программа выполняет моделирование методом Монте-Карло (то есть повторяющиеся случайные 
симуляции), чтобы исследовать эту концепцию.

(На самом деле это не парадокс, это просто удивительный результат.)''')
    
    # Создаем кортех названий месяцев по порядку
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    
    while True: # Запрашиваем, пока пользователь не введет допустимое значение
        print('Сколько дней рождения мне сгенирировать? (Максимум 100)')
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            num_birthdays = int(response)
            break
    print()
    
    # Генерируем и отображаем дни рождения:
    print('Это', num_birthdays, 'дней рождений:')
    birthdays = get_birthdays(num_birthdays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            # Выводим запятую для каждого дня рождения после первого
            print(', ', end='')
        month_name = MONTHS[birthday.month - 1]
        
        date_text = f'{month_name} {birthday.day}'
        print(date_text, end='')
    print('\n\n')
    
    # Выясняем, встречаются ли два совпадающих дня рождения
    match = get_match(birthdays)
    
    # Отображаем результаты:
    print('В этой демонстрации, ', end='')
    if match != None:
        month_name = MONTHS[match.month - 1]
        date_text = f'{month_name} {match.day}'
        print('у многих людей день рождения ', date_text)
    else:
        print('нет совпадающих дней рождений.')
    print()
    
    # Производим 100 000 операций имитационного моделирования:
    print('Генерируем', num_birthdays, 'случайных дней рождений 100 000 раз...')
    input('Нажмите Enter, чтобы начать...')
    
    print('Давайте запустим еще 100 000 имитаций.')    
    sim_match = 0  # Число операций моделирования с совпадающими днями рождения
    for i in range(100_000):
        # Отображаем сообщение о ходе выполнения каждые 10 000 операций:
        if i % 10_000 == 0:
            print(i, 'имитаций выполнено...')
        birthdays = get_birthdays(num_birthdays)
        if get_match(birthdays) != None:
            sim_match += 1
    print('100 000 имитаций выполненно.')
    
    # Отображаем результаты имитационного моделирования:
    probability = round(sim_match / 100_000 * 100, 2)
    print('Из 100 000 имитаций', num_birthdays, 'людей. Дни рождения, которых в группе')
    print('совпадают', sim_match, 'раз. Это означает, что у', num_birthdays, 'людей')
    print('с вероятностью', probability, '% совпадают дни рождения в их группе.')
    print('Это более чем достаточно, чем я ожидал.')
    

if __name__ == '__main__':
    main()