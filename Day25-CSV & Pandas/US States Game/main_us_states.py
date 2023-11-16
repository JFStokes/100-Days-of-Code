#####################################################################
#                          US STATES GAME                           #
#####################################################################
# Creates a game where the player is given a blank map of the US. The
#   player must enter the name of each state. If the entered name is
#   correct, the name populates on top of the blank state.
# Date: 15 November 2023        Author: Josh Stokes
import turtle
import pandas as p

t = turtle.Turtle()
screen = turtle.Screen()
data = p.read_csv('50_states.csv')
print(data)


#####################################################################
screen.exitonclick()