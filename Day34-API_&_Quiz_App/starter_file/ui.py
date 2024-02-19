import os
import tkinter
from quiz_brain import QuizBrain

DIR_PATH = os.path.dirname(__file__)
TRUE_PNG_PATH = DIR_PATH + "\\images\\true.png"
FALSE_PNG_PATH = DIR_PATH + "\\images\\false.png"
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        # Score Label - 20 padding - c1, r0.
        self.score_label = tkinter.Label(font=("Arial", 14, "bold"),
                                         background=THEME_COLOR, foreground="#FFFFFF",
                                         text="Score: 0", justify="center",
                                         padx=20, pady=20)
        self.score_label.grid(column=1, row=0)

        # Question Canvas - Arial, 20, italic, 300w, 250h, 20 padding - c0, r1, s2.
        self.question_canvas = tkinter.Canvas(self.window,
                                              width=300, height=250)
        self.question_text = self.question_canvas.create_text(150, 100,
                                                              text="Question",
                                                              width=280, justify="center",
                                                              font=("Arial", 20, "italic"))
        self.question_canvas.grid(column=0, row=1, columnspan=2,
                                  padx=20, pady=20)

        # True Button - c0, r2.
        self.true_png = tkinter.PhotoImage(file=TRUE_PNG_PATH)
        self.true_button = tkinter.Button(image=self.true_png,
                                          highlightthickness=0,
                                          command=self.answer_true)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        # False Button - c1, r2.
        self.false_png = tkinter.PhotoImage(file=FALSE_PNG_PATH)
        self.false_button = tkinter.Button(image=self.false_png,
                                           highlightthickness=0,
                                           command=self.answer_false)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()


        self.window.mainloop()
    
    # Gets the next question.
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(
                self.question_text,
                text=f"You've complete the quiz with {self.quiz.score} of 10 correct questions."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    # True Button command.
    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    # False Button command.
    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_correct: bool):
        if is_correct:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.reset)

    def reset(self):
        self.question_canvas.config(bg="white")
        self.get_next_question()
