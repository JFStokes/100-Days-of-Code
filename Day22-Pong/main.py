#####################################################################
#                               PONG                                #
#####################################################################
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from text import Text
# import time

# Initializes the screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Josh\'s Pong Game')
screen.tracer(0)

# Create game objects.
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
b = Ball()
r_text = Text()
r_text.goto(200, 275)
l_text = Text()
l_text.goto(-200, 275)


# Moves the ball by changing 'b.moving' to true/false.
def start_moving_ball():
    if not b.moving:
        b.moving = True
        print('Ball Served.')
    else:
        b.moving = False

# Dectects input.
screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')
screen.onkey(start_moving_ball, 'space')
screen.onkey(b.sim_bounce, 'b')

############################ Main Loop ##############################
game_is_running = True
while game_is_running:

    # Used to pause between updates.
    # time.sleep(0.01)

    # Updates the screen each frame.
    screen.update()

    # Moves the ball when 'space' is pressed.
    if b.moving:
        b.move_ball()  
    
    # Detects collision with top/bottom to bounce the ball.
    b.bounce()

    # Detects collision with the right paddle.
    if b.distance(r_paddle) < 50 and b.xcor() < 330:
        b.xspeed *= -1

    # Detects collision with the left paddle.
    if b.distance(l_paddle) < 50 and b.xcor() > -330:
        b.xspeed *= -1
    
    # Detects collision with left/right side of screen.
    b.ball_missed(b.xcor())

    # Display Scores.
    r_text.show_score(r_paddle.points)
    l_text.show_score(l_paddle.points)

############################## Close ################################
screen.exitonclick()
