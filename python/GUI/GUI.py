from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import math

methods = ["Через основание и высоту",
           "Через две стороны и угол"]

def show_result(area):
    area = round(area, 2)

    messagebox.showinfo('Результат', f'Площадь треугольника = {area}')

def calc_area_BAH(base, height):
    base = float(base)
    height = float(height)
    area = float(base*height/2)
    show_result(area)

def calc_area_SAA(a, b, alpha, angle):
    a=float(a)
    b=float(b)
    alpha=float(alpha)

    if angle=='degrees':
        alpha=to_rad(alpha)
    area=(a*b*math.sin(alpha))/2
    show_result(area)

def to_rad(deg):
    return math.pi/180*deg

def selected(event):
    selection = combobox.get()

    if selection == 'Через основание и высоту':
        method_BAH()

    if selection == 'Через две стороны и угол':
        method_SAA()

def method_BAH():
    clear_extra_widgets()
    base_lbl = Label(
        frame,
        text='Основание треугльника'
    )
    base_lbl.grid(row=3, column=1, pady=10)
    base_ent = Entry(
        frame
    )
    base_ent.grid(row=3, column=2)
    base_ent.focus()

    h_lbl = Label(
        frame,
        text='Высота треугольника'
    )
    h_lbl.grid(row=4, column=1, pady=10)
    h_ent = Entry(
        frame
    )
    h_ent.grid(row=4, column=2)

    area_btn = Button(
        frame,
        text='Рассчитать площаль',
        command=lambda: calc_area_BAH(base_ent.get(), h_ent.get())
    )
    area_btn.grid(row=5, column=2)

def method_SAA():
    clear_extra_widgets()
    a_lbl = Label(
        frame,
        text='Сторона a'
    )
    a_lbl.grid(row=3, column=1, pady=10)
    a_ent = Entry(
        frame
    )
    a_ent.grid(row=3, column=2)
    
    b_lbl = Label(
        frame,
        text='Сторона b'
    )
    b_lbl.grid(row=4, column=1, pady=10)
    b_ent = Entry(
        frame
    )
    b_ent.grid(row=4, column=2)
    angle_lbl = Label(
        frame,
        text='Угол'
    )
    angle_lbl.grid(row=5, column=1, pady=10)
    angle_ent = Entry(
        frame
    )
    angle_ent.grid(row=5, column=2)
    
    var = StringVar()
    var.set('degrees')
    degrees_rbt = Radiobutton(frame, text='град.', variable=var, value='degrees')
    radians_rbt = Radiobutton(frame, text='рад.', variable=var, value='radians')

    degrees_rbt.grid(row=5, column=3)
    radians_rbt.grid(row=5, column=4)

    calc_btn = Button(
        frame,
        text='Рассчитать площадь',
        command=lambda: calc_area_SAA(a_ent.get(), b_ent.get(), angle_ent.get(), var.get())
    )
    calc_btn.grid(row=6, column=2)

window = Tk()

window.title('Калькулятор площади треугольника')
window.geometry('500x250')

frame = Frame(
    window,
    padx=10,
    pady=10,
    relief=RAISED,
    borderwidth=5,
)

lbl = Label(
    frame,
    text='Выберите способ расчета',
    background='gray',
)
lbl.grid(row=1, column=1)

combobox = Combobox(
    frame,
    values=methods,
    width=30,
    state='readonly'
)
combobox.grid(row=2, column=1)
combobox.set('Черезе основание и высоту')
combobox.bind('<<ComboboxSelected>>', selected)

global_widgets = frame.winfo_children()
def clear_extra_widgets():
    for widget in frame.winfo_children():
        if widget not in global_widgets:
            widget.destroy()


frame.pack(expand=True)

window.mainloop()