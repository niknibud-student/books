""" Программа "Охотник за пузырями"


    Returns:
        move_ship(event: Event): Функция движения подлодки
        create_buble(): Функция создания пузырей
        move_bubles(): Функция движения пузырей
        get_coords(id_num: int) -> Tuple[float]: Функция получения координат объекта
        del_buble(id_num: int): Функция удаления пузыря из списков настроек пузыря
        clean_up_bubs(): Функция удаления пузырей, которые улетели за границу игры
        distance(id1: int, id2: int) -> float: Функция определения расстояния между объектами
        collision() -> int: Функция определяющая, возникающие столкновения подлодки и пузыря,
                            возвращает количество баллов за сбитый пузырь
        show_score(score_: int): Функция, показывающая количество баллов
        show_time(time_left: int): Функция, показывающая оставшееся время игры
"""
from math import sqrt
from tkinter import Event, Tk, Canvas
from random import randint
from time import sleep, time
from typing import Tuple, List


HEIGHT = 500  # Высота окна
WIDTH = 800  # Ширина окна
SHIP_SPEED = 10  # Скорость подлодки
SHIP_R = 5 # Радиус корабря
MID_X = WIDTH / 2  # Центр экрана
MID_Y = HEIGHT / 2  # Центр экрана
MIN_BUB_R = 10   # Минимальный радиус пузыря
MAX_BUB_R = 30  # Минимальный радиус пузыря
MAX_BUB_SPEED = 10  # Максимальная скорость пузыря
GAP = 100  # Расстояние формирования пузыря за экраном
BUB_CHANCE = 10  # Частота формирования пузырей
TIME_LIMIT = 30  # Ограничение времени игры
BONUS_SCORE = 1000  # Количество очков, при котором начисляется дополнительное время


def move_ship(event: Event) -> None:
    """Движение лодки с помощью стрелок клавиатуры

    Args:
        event (Event): событие нажания кнопки
    """
    key = event.keysym
    if key == 'Up':
        canvas.move(ship_id, 0, -SHIP_SPEED)
        canvas.move(ship_id2, 0, -SHIP_SPEED)
    elif key == 'Down':
        canvas.move(ship_id, 0, SHIP_SPEED)
        canvas.move(ship_id2, 0, SHIP_SPEED)
    elif key == 'Left':
        canvas.move(ship_id, -SHIP_SPEED, 0)
        canvas.move(ship_id2, -SHIP_SPEED, 0)
    elif key == 'Right':
        canvas.move(ship_id, SHIP_SPEED, 0)
        canvas.move(ship_id2, SHIP_SPEED, 0)



def create_buble() -> None:
    """ Создание пузырей

        Пузыри создаются за правой границей экрана.
        Вертикальное положение, радиус и скорость движения пузырей выбираются случайным образом
    """
    coord_x = WIDTH + GAP
    coord_y = randint(0, HEIGHT)
    buble_radius = randint(MIN_BUB_R, MAX_BUB_R)
    bub_id.append(canvas.create_oval(
        coord_x - buble_radius,
        coord_y - buble_radius,
        coord_x + buble_radius,
        coord_y + buble_radius,
        outline='white'
    ))
    bub_r.append(buble_radius)
    bub_speed.append(randint(1, MAX_BUB_SPEED))


def move_bubbles() -> None:
    """Движение пузырей """
    for i, bub in enumerate(bub_id):
        canvas.move(bub, -bub_speed[i], 0)


def get_coords(id_num: int) -> Tuple[float]:
    """Определение координат объектов

    Args:
        id_num (int): id объекта

    Returns:
        Tuple[float]: точка положения центра объекта в виде кортежа
    """
    pos = canvas.coords(id_num)
    coord_x = (pos[0] + pos[2]) / 2
    coord_y = (pos[1] + pos[3]) / 2
    return coord_x, coord_y


def del_bubble(id_num: int) -> None:
    """Удаление пузыря
        Удаляем из списков радиусов, скоростей и объектов пузырей

    Args:
        id_num (int): номер пузыря в списках
    """
    del bub_r[id_num]
    del bub_speed[id_num]
    canvas.delete(bub_id[id_num])
    del bub_id[id_num]


def clean_up_bubs() -> None:
    """Удаление пузырей, которые уплыли за край холста """
    for i in range(len(bub_id) - 1, -1, -1):
        coord_x = get_coords(bub_id[i][0])
        if coord_x < -GAP:
            del_bubble(i)


def distance(id1: int, id2: int) -> float:
    """Определяет расстояние между подлодкой и пузырем

    Args:
        id1 (int): id подлодки
        id2 (int): id пузыря

    Returns:
        float: расстояние между центрами подлодки и пузыря
    """
    coord_x1, coord_y1 = get_coords(id1)
    coord_x2, coord_y2 = get_coords(id2)
    return sqrt((coord_x2 - coord_x1) ** 2 + (coord_y2 - coord_y1) ** 2)


def collision() -> int:
    """Обработывает коллизии и считает очки

        Очки за сбитый пузырь считаются как сумма радиуса пузыря и его скорости

    Returns:
        int: количество очков
    """
    points = 0
    for id_bub in range(len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[id_bub]) < (SHIP_R + bub_r[id_bub]):
            points += (bub_r[id_bub] + bub_speed[id_bub])
            del_bubble(id_bub)
    return points


def show_score(score_: int) -> None:
    """Отображение счёта игры

    Args:
        score (int): Количество баллов
    """
    canvas.itemconfig(score_text, text=str(score_))


def show_time(time_left: int) -> None:
    """Отображение времени игры

    Args:
        time_left (int): Прошедшее время игры
    """
    canvas.itemconfig(time_text, text=str(time_left))

window = Tk()
window.title('Охотник за пузырями')

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
canvas.pack()

# Описание подлодки, ее первоначального положения и привязка обработчика движения
ship_id = canvas.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship_id2 = canvas.create_oval(0, 0, 30, 30, outline='red')
canvas.move(ship_id, MID_X, MID_Y)
canvas.move(ship_id2, MID_X, MID_Y)
canvas.bind_all('<Key>', move_ship)

# Отображение полей Времени и Счёта
canvas.create_text(50, 30, text='ВРЕМЯ:', fill='white')
canvas.create_text(150, 30, text='СЧЁТ:', fill='white')
time_text = canvas.create_text(50, 50, fill='white')
score_text = canvas.create_text(150, 50, fill='white')

bub_id: List[int] = list()  # Список пузырей
bub_r: List[int] = list()  # Список радиусов пузырей
bub_speed: List[int] = list()  # Список скоростей пузырей
score: int = 0  # Количество очков
bonus: int = 0  # Количество раз, получения бонусного времени
end = time() + TIME_LIMIT

# MAIN GAME LOOP
while time() < end:
    if randint(1, BUB_CHANCE) == 1:
        create_buble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)

# Отображение информации после окончания игры
canvas.create_text(MID_X, MID_Y, text='ИГРА ОКОНЧЕНА', fill='white', font=('Helvetica', 30))
canvas.create_text(MID_X, MID_Y + 30, text='СЧЁТ:{}'.format(score), fill='white')
canvas.create_text(
    MID_X, MID_Y + 45,
    text='Бонус времени: {}'.format(bonus * TIME_LIMIT),
    fill='white'
)

window.mainloop()
