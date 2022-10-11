""" Программа эмуляции броска кубика
"""
from tkinter import Tk, Text, Button, END
from random import randint


def roll() -> None:
    """ Бросок кубика """
    text.delete(0.0, END)
    text.insert(END, str(randint(1, 6)))


window = Tk()
text = Text(window, width=1, height=1)
button_a = Button(window, text='Нажми для броска!', command=roll)
text.pack()
button_a.pack()

window.mainloop()
