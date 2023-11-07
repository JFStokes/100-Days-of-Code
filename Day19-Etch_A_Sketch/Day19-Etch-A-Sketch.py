#####################################################################
#                           ETCH-A-SKETCH                           #
#####################################################################
from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


############################ FUNCTIONS ##############################
def move_forwards():
  tim.forward(10)

def move_back():
  tim.backward(10)

def turn_left():
  tim.left(5)

def turn_right():
  tim.right(5)

def reset():
  screen.resetscreen()


############################ MAIN LOOP ##############################
screen.listen()
screen.onkey(move_forwards, 'Up')
screen.onkey(move_back, 'Down')
screen.onkey(turn_left, 'Left')
screen.onkey(turn_right, 'Right')
screen.onkey(reset, 'c')
screen.exitonclick()