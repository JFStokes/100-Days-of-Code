############################### TEXT ################################
from turtle import Turtle

class Text(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()

    def show_score(self, score):
        self.write(f'Score: {score}', False, align='center',
                   font=('Arial', 12, 'normal'))