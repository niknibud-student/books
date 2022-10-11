""" Окно Tkinter с двумя кнопками """
from tkinter import Tk, Button

def btn_a_action() -> None:
    """ Печатает спасибо! """
    print('Спасибо!')

def btn_b_action():
    """ Печатает ругательство! """
    print('Ouch! That hurt!')

window = Tk()

button_a = Button(window, text='Нажми меня!', command=btn_a_action)
button_b = Button(window, text='Не нажимай!', command=btn_b_action)
button_a.pack()
button_b.pack()

window.mainloop()
