#####################################################################
#                          US STATES GAME                           #
#####################################################################
# Creates a game where the player is given a blank map of the US. The
#   player must enter the name of each state. If the entered name is
#   correct, the name populates on top of the blank state.
# Date: 15 November 2023        Author: Josh Stokes
import os
import turtle
import pandas
from text import Text
from scoreboard import ScoreBoard

CWD = os.getcwd()

# Variable for the image of the US map.
map_image = CWD + '\\blank_states_img.gif'

# Screen setup.
screen = turtle.Screen()
screen.title('Josh\'s US States Game')
screen.addshape(map_image) # Gives the map image to 'screen'.
screen.tracer(0)
turtle.shape(map_image) # Gives screen turtle the map image.

# Import data from csv and put States in a list.
data = pandas.read_csv('50_states.csv')
state_list = data['state'].to_list()

# Create a list to store used player answers.
used_states = []

# Create the scoreboard.
sb = ScoreBoard(-250, 250)

# Create High Scores.
hsm = ScoreBoard(-350, -260)
hs = ScoreBoard(-350, -260)

# Receive the player's name.
player_name = screen.textinput(title='Save your score!',
                                       prompt='Enter your name:')
player_name = player_name.title()

# Creat message box.
msg = ScoreBoard(0, 300)
msg_text = f'Hello {player_name}!'

############################ Game Loop ##############################
game_running = True
while game_running:

    # Updates the screen at the beginning of each frame.
    screen.update()

    # Update the scoreboard.
    sb.showscore()

    # Update message box.
    msg.show_message(msg_text)

    # Show the High Scores.
    hsm.high_score_title()
    hs.showhighscores()

    # Creates popup window for player input.
    player_answer = screen.textinput(title='Guess the State', 
                                    prompt='What is another State?')
    player_answer = player_answer.title()

    # Commands to end the game.
    if player_answer == 'Quit' \
    or player_answer == 'Exit' \
    or player_answer == 'Stop' \
    or player_answer == 'Save':
        game_running = False
    
    # State is correct.
    if player_answer in state_list:

        # Checks if state has already been used.
        if player_answer in used_states: # Already used.
            msg_text = f'{player_answer} already used!'
        else: # Not used.
            msg_text = f'Yes! {player_answer} is one of the states!'

            # Adds state to the 'used' list.
            used_states.append(player_answer)

            # Gets the x/y from csv file.
            answer_state = data[data.state == player_answer]
            state_x = int(answer_state.x)
            state_y = int(answer_state.y)

            # Creates a label on top of the state.
            new_state = Text(player_answer, state_x, state_y)

            # Adds a point to the player's score.
            sb.score += 1
    
    # State is not correct.
    else:
        msg_text = f'{player_answer} is not one of the states.'
    

#####################################################################
# Adds player name & score to dict.
new_record = {
    "player": player_name,
    "score": sb.score
}

# Saves dict to 'scores.json'.
sb.save_score(new_record)

exit()
