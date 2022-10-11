""" Программа рисования кругов случайного диаметра, в случайном месте
    одного из четырех цветов (розовый, оранжевый, пурпурный, желтый)
"""
from tkinter import Tk, Canvas
from random import randint, choice


SIZE = 500

window = Tk()
canvas = Canvas(window, width=SIZE, height=SIZE)
canvas.pack()

while True:
    color = choice(['pink', 'orange', 'purple', 'yellow'])
    x0 = randint(0, SIZE)
    y0 = randint(0, SIZE)
    d = randint(0, SIZE / 5)
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=color)
    window.update()
