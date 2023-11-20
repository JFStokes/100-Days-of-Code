# Object used to create each state's label.
from turtle import Turtle


class Text(Turtle):
    def __init__(self, name, x_coor, y_coor):
        super().__init__()
        self.hideturtle()
        self.name = name
        self.xcor = x_coor
        self.ycor = y_coor
        self.color('black')
        self.penup()
        self.goto(self.xcor, self.ycor)
        self.write(self.name, False, align='center',
                   font=('Arial', 8, 'normal'))
