############################## PADDLE ###############################
from turtle import Turtle


class Paddle:
    def __init__(self) -> None:
        self.width = 20
        self.height = 100
        self.x_pos = 350
        self.y_pos = 0
        self.paddle_squares = [(350, 0), (350, -20), (350, -40)]
    
    def create_paddle(self):
        for position in self.paddle_squares:
            self.add_paddle_squares(position)
    
    def add_paddle_squares(self, position):
        p = Turtle('square')
        p.color('white')
        p.penup()
        p.goto(position)
