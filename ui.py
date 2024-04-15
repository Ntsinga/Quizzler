from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=300, height=400)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz

        self.score_label = Label(text=f"Score=0", bg=THEME_COLOR, font=("Arial", 15, "normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text="vgwevegw", fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.is_true)
        self.true_button.grid(column=0, row=4)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.is_false)
        self.false_button.grid(column=1, row=4)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=quiz_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score={self.quiz.score}")
