#####################################################################
#                          US STATES GAME                           #
#####################################################################
# Creates a game where the player is given a blank map of the US. The
#   player must enter the name of each state. If the entered name is
#   correct, the name populates on top of the blank state.
# Date: 15 November 2023        Author: Josh Stokes
import turtle
import pandas
from text import Text

# Variable for the image of the US map.
map_image = 'blank_states_img.gif'

# Screen setup.
screen = turtle.Screen()
screen.title('Josh\'s US States Game')
screen.addshape(map_image)
screen.tracer(0)
turtle.shape(map_image)

# Import data from csv and put States in a list.
data = pandas.read_csv('50_states.csv')
state_list = data['state'].to_list()


############################ Game Loop ##############################
game_running = True
while game_running:

    # Updates the screen at the beginning of each frame.
    screen.update()

    # Creates popup window for player input.
    player_answer = screen.textinput(title='Guess the State', 
                                    prompt='What is another State?')
    player_answer = player_answer.title()
    print(player_answer)

    # Commands to end the game.
    if player_answer == 'Quit' \
    or player_answer == 'Exit' \
    or player_answer == 'Stop':
        game_running = False
        exit()
    
    if player_answer in state_list:
        print(f'Yes, {player_answer} is one of the states!')

        # Gets x and y of player input.
        answer_state = data[data.state == player_answer]
        state_x = int(answer_state.x)
        state_y = int(answer_state.y)
        print(f'{player_answer} X is {state_x} and Y is {state_y}')
        new_state = Text(player_answer, state_x, state_y)
    else:
        print(f'Sorry, {player_answer} is not one of the states.')


#####################################################################
screen.exitonclick()
