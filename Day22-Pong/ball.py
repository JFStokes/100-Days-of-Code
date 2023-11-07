############################### BALL ################################
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('white')
        self.xspeed = 2
        self.yspeed = 2
        self.goto(0, 0)
        self.moving = False
    
    def move_ball(self):
        new_x = self.xcor() + self.xspeed
        new_y = self.ycor() + self.yspeed
        self.goto(new_x, new_y)
    
    def bounce(self):
        # Bounce off top/bottom of screen.
        if self.ycor() <= -280 or self.ycor() >= 290:
            self.yspeed = self.yspeed * -1
        
    def sim_bounce(self):
        self.xspeed = self.xspeed * -1
