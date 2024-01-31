#####################################################################
#                         100 DAYS OF CODE                          #
#                              DAY 18                               #
#                           TURTLE & GUI                            #
#####################################################################
from turtle import Turtle, Screen
import os
import time
import random
import colorgram

# Get file path.
DIR_PATH = os.path.dirname(__file__)
print(f'Path is {DIR_PATH}')

# The turtle object.
timmy = Turtle()
timmy.hideturtle() # Hides the turtle.

# Creates the screen object.
screen = Screen()
print(f'Screen size is {screen.screensize()}')
screen.title('Josh\'s Coding Practice')
screen.colormode(255)

########################### CHALLENGE 1 #############################
# Drawing a square
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.penup()
timmy.forward(50)

########################### CHALLENGE 2 #############################
# Draw a dashed line.
for n in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

timmy.right(90)
timmy.forward(300)
timmy.right(90)
timmy.forward(300)
timmy.pendown()

########################### CHALLENGE 3 #############################
# Draw different shapes in random colors.
screen.colormode(255)
shape_sides = 3
for shape in range(7):
    shape_color1 = (random.randint(0, 255))
    shape_color2 = (random.randint(0, 255))
    shape_color3 = (random.randint(0, 255))
    angle = 360 / shape_sides
    for sides in range(shape_sides):
        timmy.pencolor((shape_color1, shape_color2, shape_color3))
        timmy.forward(50)
        timmy.right(angle)
    shape_sides += 1

########################### CHALLENGE 4 #############################
# Reset and move to new location.
screen.colormode(1)
timmy.pencolor('black')
timmy.forward(300)
screen.colormode(255)


# Draw a random walk in random colors.
turns = 50
for turn in range(turns):
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    timmy.pencolor(r, g, b)
    dir = random.randint(1, 2)
    if dir == 1:
        timmy.right(90)
        timmy.forward(10)
    else:
        timmy.left(90)
        timmy.forward(10)

########################### CHALLENGE 5 #############################
# Draw a Spirgraph.
screen.clearscreen()
screen.resetscreen()
screen.colormode(255)
timmy.reset()
timmy.speed(0)
heading = 0
timmy.setheading(heading)
circles = 50
angles = 360 / circles
for circles in range(circles):
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    timmy.pencolor(r, g, b)
    timmy.circle(100)
    heading += angles
    timmy.setheading(heading)

time.sleep(5)

##################### Hirst Painting Project ########################
# Preview Hirst Painting.
screen.clearscreen()
screen.bgpic(DIR_PATH + '/Day18 Hirst Painting.png')
screen.update()

# Extract 10 colors from an image.
colors = colorgram.extract(DIR_PATH + '/Day18 Hirst Painting.jpg', 18)
rgb_colors = []
for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
time.sleep(10)


# Create Hirst Painting.
screen.clearscreen()
timmy.penup()
screen.colormode(255)
timmy_x = -440
timmy_y = 330
timmy.setposition(timmy_x, timmy_y)
rows = 10
cols = 10
for row in range(rows):
    dot_color = rgb_colors[random.randint(0, 17)]
    timmy_x = -400
    timmy.setx(timmy_x)
    timmy_y -= 60
    timmy.sety(timmy_y)
    timmy.dot(20, dot_color)
    for col in range(cols - 1):
        dot_color = rgb_colors[random.randint(0, 9)]
        timmy_x += 80
        timmy.setx(timmy_x)
        timmy.dot(20, dot_color)


############################ CONCLUSION #############################
# Exits turtle when 'X' clicked.
screen.exitonclick()
