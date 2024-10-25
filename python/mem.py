# memory card GUI application
from tkinter import *

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

window=QWidget()
window.setLayout(layout_card)
