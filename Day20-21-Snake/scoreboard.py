############################ Scoreboard #############################
from turtle import Turtle


# Class for ScoreBoard object (inhereted from Turtle object).
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize Turtle inside ScoreBoard.
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

    # Method to display text on screen.
    def show_score(self, score):
        self.score = score
        self.write(f'Score: {self.score}',
                   False,
                   align='center',
                   font=('Arial', 12, 'normal'))

    def game_over(self, game_running):
        if not game_running:
            self.goto(0, 0)
            self.write('GAME OVER',
                       False,
                       align='center',
                       font=('Arial', 32, 'normal'))
