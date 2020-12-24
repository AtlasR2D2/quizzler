import tkinter as tk
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
PADDING = 20
SCORE_FONT_COLOR = "white"
QUESTION_BG_COLOR = "white"
QUESTION_FONT = ("Arial", 14, "italic")
QUESTION_HEIGHT = 250
QUESTION_WIDTH = 300
BOOLEAN_IMAGE_HEIGHT = 97
BOOLEAN_IMAGE_WIDTH = 100

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.question = None
        self.answer = None
        self.guess: str
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=PADDING, pady=PADDING)
        # Score Label
        self.score_label = tk.Label(text=f"Score: {self.score}", fg=SCORE_FONT_COLOR, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Question Visual
        self.q_canvas = tk.Canvas(width=QUESTION_WIDTH, height=QUESTION_HEIGHT, bg=QUESTION_BG_COLOR, highlightthickness=0)
        self.question_text = self.q_canvas.create_text(QUESTION_WIDTH / 2, QUESTION_HEIGHT * 0.50, text="SAMPLE QUESTION",
                                        font=QUESTION_FONT, width=QUESTION_WIDTH*0.8)
        self.q_canvas.grid(row=1, column=0, columnspan=2, pady=PADDING, sticky="w")

        # True Button
        true_img = tk.PhotoImage(file=r".\images\true.png")
        self.true_button = tk.Button(image=true_img, highlightthickness=0, command=self.true_click)
        self.true_button.grid(row=2, column=1)

        # False Button
        false_img = tk.PhotoImage(file=r".\images\false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0, command=self.false_click)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def update_score(self):
        self.score_label["text"] = f"Score: {self.quiz.score}"

    def true_click(self):
        self.guess = "True"
        self.give_feedback()

    def false_click(self):
        self.guess = "False"
        self.give_feedback()

    def give_feedback(self):
        if self.quiz.check_answer(self.guess):
            self.q_canvas.config(bg="green")
        else:
            self.q_canvas.config(bg="red")
        self.window.update()
        time.sleep(1)
        self.update_score()
        self.get_next_question()


    def get_next_question(self):
        self.q_canvas.config(bg=QUESTION_BG_COLOR)
        self.window.update()
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
        else:
            q_text = "You've reached the end of the quiz."
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.q_canvas.itemconfig(self.question_text, text=q_text)