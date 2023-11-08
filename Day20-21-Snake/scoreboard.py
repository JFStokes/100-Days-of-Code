############################ Scoreboard #############################
from turtle import Turtle


# Class for ScoreBoard object (inhereted from Turtle object).
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize Turtle inside ScoreBoard.
        self.color('white')
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

    # Method to display text on screen.
    def show_score(self):
        self.clear()
        self.write(f'Score: {self.score}. High Score: {self.high_score}',
                   False,
                   align='center',
                   font=('Arial', 12, 'normal'))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0


    # def game_over(self, game_running):
    #     if not game_running:
    #         self.goto(0, 0)
    #         self.write('GAME OVER',
    #                    False,
    #                    align='center',
    #                    font=('Arial', 32, 'normal'))
