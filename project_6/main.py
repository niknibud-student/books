""" Программа 'Рисовательный автомат'
    Построена на основе модуля turtle
"""
from turtle import forward, backward, getscreen, left, right, penup, pendown, reset


def turtle_controller(do_: str, val: int = 0) -> None:
    """Функция, выполняющая команды

    Args:
        do (str): команда
        val (int): значение расстояния
    """
    do_ = do_.upper()
    commands = {
        'F': forward,
        'B': backward,
        'R': right,
        'L': left,
        'U': penup,
        'D': pendown,
        'N': reset
    }

    if do_ in commands:
        if val > 0:
            commands[do_](val)
        else:
            commands[do_]()
    else:
        print('Неизвестная команда')


def string_artist(program: str) -> None:
    """Разделяет программу на команды

    Args:
        program (str): строка программы
    """
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num = int(command[1:])
        print(command, ':', cmd_type, num)
        turtle_controller(cmd_type, num)


if __name__ == '__main__':
    INSTRUCTIONS = '''Ввведите программу для черепашки:
например, F100-R45-U-F100-L45-D-F100-R90-B50
N = Новый рисунок
U/D = Перо поднять/опустить
F100 = вперед 100
B50 = назад 50
R90 = Повернуться вправо на 90 градусов
L45 = Повернуться влево на 45 градусов'''

    screen = getscreen()
    while True:
        t_program = screen.textinput('Рисовательный автомат', INSTRUCTIONS)
        print(t_program)
        if t_program is None or t_program.upper() == 'END':
            break
        string_artist(t_program)
