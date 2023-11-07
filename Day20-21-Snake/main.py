#####################################################################
#                        Josh's Snake Game                          #
#####################################################################
import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

############################### Setup ###############################
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Josh\'s Snake Game')
screen.tracer(0)

# Create snake, food, scoreboard, and game over objects.
snake = Snake()
food = Food()
sb = ScoreBoard()
go = ScoreBoard()

############################# Controls ##############################
# Listens for input.
screen.listen()

# Controls.
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

############################ Main Loop ##############################
running = True
score = 0
while running:

    # Re-draw the screen each frame.
    screen.update()

    # Pause the script between each frame.
    time.sleep(0.2)

    # Move the snake each frame.
    snake.move()

    # Detect snake collision with food.
    if snake.head.distance(food) < 20:  # 20 pixels.
        food.refresh()
        snake.extend()
        sb.clear()
        score += 1

    # Detect snake collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            running = False

    # Display Score.
    sb.show_score(score)

    # Detect collision with walls.
    if snake.head.xcor() > 280 or\
    snake.head.xcor() < -280 or\
    snake.head.ycor() > 280 or\
    snake.head.ycor() < -280:
        running = False

    go.game_over(running)

############################### Exit ################################
screen.exitonclick()
