#####################################################################
#                               PONG                                #
#####################################################################
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Josh\'s Pong Game')
screen.tracer(0)


p = Paddle()


############################ Main Loop ##############################
game_is_running = True
while game_is_running:

    screen.update()

    p.create_paddle()

screen.exitonclick()
