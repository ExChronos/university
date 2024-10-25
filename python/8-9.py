from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import math

methods = ['Куб',
           'Сфера',
           'Прямоугольный параллелипипед']

# выводим результат на экран
def show_result(volume):
    volume=round(volume, 2)

    if volume < 0:
        messagebox.showerror('Отрицательный объем', 'У фигуры получился отрицательный объем')
    messagebox.showinfo('Объем фигуры', f'Объем заданной фигуры равен {volume}')

# различные функции для подсчета объема
def calc_vol_sqr(a):
    a = float(a)
    volume = a*a*a
    show_result(volume)

def calc_vol_sp(r):
    r = round(float(r), 3)
    volume = 4/3 * math.pi * (r**3)
    show_result(volume)
    
def calc_vol_sq_par(l, w, h):
    l = round(float(l), 2)
    w = round(float(w), 2)
    h = round(float(h), 2)

    volume = l*w*h

    show_result(volume)

# выбор метода
def selected(event):
    selection = combobox.get()

    if selection == 'Куб':
        vol_cube()
    if selection == 'Сфера':
        vol_sp()
    if selection == 'Прямоугольный параллелипипед':
        vol_sq_par()

# различные варианты выбора методов
def vol_cube():
    clear_extra_widgets()

    a_lbl = Label(
        frame,
        text='Сторона куба'
    )
    a_lbl.grid(row=3, column=1, pady=10)
    a_ent = Entry(
        frame
    )
    a_ent.focus()
    a_ent.grid(row=3, column=2)

    volume_btn = Button(
        frame,
        text='Рассчитать объем',
        command=lambda: calc_vol_sqr(a_ent.get())
    )
    volume_btn.grid(row=4, column=2)

def vol_sp():
    clear_extra_widgets()

    r_lbl = Label(
        frame,
        text='Радиус сферы'
    )
    r_lbl.grid(row=3, column=1, pady=10)

    r_ent = Entry(
        frame
    )
    r_ent.grid(row=3, column=2)
    r_ent.focus()

    volume_btn = Button(
        frame,
        text='Рассчитать объем',
        command=lambda: calc_vol_sp(r_ent.get())
    )
    volume_btn.grid(row=4, column=2)

def vol_sq_par():
    clear_extra_widgets()

    l_lbl = Label(frame, text='Длина паралеллепипеда')
    l_lbl.grid(row=3, column=1, pady=10)

    l_ent = Entry(frame)
    l_ent.grid(row=3, column=2)

    w_lbl = Label(frame, text='Ширина параллелепипеда')
    w_lbl.grid(row=4, column=1, pady=10)

    w_ent = Entry(frame)
    w_ent.grid(row=4, column=2)

    h_lbl = Label(frame, text='Высота параллелепипеда')
    h_lbl.grid(row=5, column=1, pady=10)

    h_ent = Entry(frame)
    h_ent.grid(row=5, column=2)

    volume_btn = Button(
        frame,
        text='Рассчитать объем',
        command=lambda: calc_vol_sq_par(l_ent.get(), w_ent.get(), h_ent.get())
    )
    volume_btn.grid(row=6, column=2)


window = Tk()

window.title('Калькулятор объемных фигур')
window.geometry('700x400')

frame = Frame(
    padx=10,
    pady=10,
    relief=RAISED,
    borderwidth=10
)

choose_lbl = Label(
    frame,
    text='Выберите фигуру',
    background='gray',
    borderwidth=10
)
choose_lbl.grid(row=1, column=1, pady=10)

combobox = Combobox(
    frame,
    values=methods,
    width=30,
    state='readonly'
)

combobox.grid(row=2, column=1)
combobox.set('Куб')
combobox.bind('<<ComboboxSelected>>', selected)

global_widgets = frame.winfo_children()
def clear_extra_widgets():
    for widget in frame.winfo_children():
        if widget not in global_widgets:
            widget.destroy()

frame.pack(expand=True)

window.mainloop()