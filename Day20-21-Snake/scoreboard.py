############################ Scoreboard #############################
import os
from turtle import Turtle

current_dir = os.getcwd()
print(f'CWD is {current_dir}.')

# Class for ScoreBoard object (inhereted from Turtle object).
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize Turtle inside ScoreBoard.
        self.color('white')
        self.score = 0
        with open(f'{current_dir}\\Day20-21-Snake\\data.txt') as data:
            self.high_score = int(data.read())
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
            with open(f'{current_dir}\\Day20-21-Snake\\data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0


    # def game_over(self, game_running):
    #     if not game_running:
    #         self.goto(0, 0)
    #         self.write('GAME OVER',
    #                    False,
    #                    align='center',
    #                    font=('Arial', 32, 'normal'))
