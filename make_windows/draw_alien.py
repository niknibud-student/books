""" Интерактивный пришелец
"""
from tkinter import Tk, Canvas, Event
from tkinter.constants import HIDDEN, NORMAL


def mouth_open() -> None:
    """ Открывает рот """
    canvas.itemconfig(mouth, fill='black')


def mouth_close() -> None:
    """ Закрывает рот """
    canvas.itemconfig(mouth, fill='red')


def blink(event: Event) -> None:
    """ Пришелец закрывает глаз

    Args:
        event (Event): Событие при котором поисходит моргание
    """
    canvas.itemconfig(eye, fill='green')
    canvas.itemconfig(eyeball, state=HIDDEN)


def unblink(event: Event) -> None:
    """ Пришелец закрывает глаз

    Args:
        event (Event): Событие при котором пришелец открывает глаз
    """
    canvas.itemconfig(eye, fill='white')
    canvas.itemconfig(eyeball, state=NORMAL)


def steal_hat() -> None:
    """ Кража шляпы """
    canvas.itemconfig(hat, state=HIDDEN)
    canvas.itemconfig(words, text='Верни мою шляпу!')


def burp(event: Event) -> None:
    """ Рыгание пришельца

    Args:
        event (Event): Событие при котором пришелец рыгает
    """
    mouth_open()
    canvas.itemconfig(words, text='Буэ!')


def eye_control(event: Event) -> None:
    """ Движение зрачка

    Args:
        event (Event): Событие при котором происходит движение зрачка
    """
    key = event.keysym

    if key == 'Up':
        canvas.move(eyeball, 0, -1)
    elif key == 'Down':
        canvas.move(eyeball, 0, 1)
    elif key == 'Left':
        canvas.move(eyeball, -1, 0)
    elif key == 'Right':
        canvas.move(eyeball, 1, 0)

window = Tk()
window.attributes('-topmost', 1)
window.title('Инопланетянин')
canvas = Canvas(window, height=300, width=400)
canvas.pack()
canvas.bind_all('<Button-1>', burp)
canvas.bind_all('<KeyPress-a>', blink)
canvas.bind_all('<KeyPress-z>', unblink)
canvas.bind_all('<Key>', eye_control)

canvas.create_oval(100, 150, 300, 250, fill='green')
eye = canvas.create_oval(170, 70, 230, 130, fill='white')
eyeball = canvas.create_oval(190, 90, 210, 110, fill='black')
mouth = canvas.create_oval(150, 220, 250, 240, fill='red')
neck = canvas.create_line(200, 150, 200, 130)
hat = canvas.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')
words = canvas.create_text(200, 280, text='Я инопланетянин!')

def main() -> None:
    """ Главная функция проекта
    """
    window.mainloop()

if __name__ == '__main__':
    main()
