# Object used to display current scores and high scores.

import json
import os
from turtle import Turtle

# Get file path.
DIR_PATH = os.path.dirname(__file__)


class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color('black')
        self.score = 0
        self.penup()
        self.hideturtle()
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
    
    # Shows current score.
    def showscore(self):
        self.clear()
        self.remaining = 50 - self.score
        self.write(f'Score: {self.score} of 50. {self.remaining} to go.', 
                   False,
                   align='center',
                   font=('Arial', 12, 'normal'))
    
    # Shows list of high scores loaded from json.
    def showhighscores(self):
        self.clear()

        # Y pos of each record.
        starting_y = self.y

        with open(DIR_PATH + '/scores.json', 'r') as scores_file:
            data = json.load(scores_file)

            # Display data for each record.
            for i, score in enumerate(data, start=1):

                # Each record moves 15pix down from previous record.
                starting_y -= 15
                self.goto(self.x, starting_y)

                # Writes the data to the screen.
                self.write(f'{i}-{score["player"]}: {score["score"]}', False,
                           align='left',
                           font=('Arial', 10, 'normal'))

    # Saves current player score to json.
    def save_score(self, new_record):
        try:
            # Opens the json file.
            with open("scores.json", "r+") as file:

                # Assigns json info into a variable.
                data = json.load(file)

                # Checks if a "player" name already exists in data.
                player_exists = any(record["player"] == new_record["player"] \
                                    for record in data)
                
                # If player exists, checks previous score.
                if player_exists:
                    for record in data:
                        if record["player"] == new_record["player"]:

                            # If new score is higher, replace old score.
                            if new_record["score"] > record["score"]:
                                record["score"] = new_record["score"]
                
                # If player does not exist, creates new record.
                else:
                    data.append(new_record)
                
                # Sorts the scores from highest\lowest.
                data.sort(key=lambda x: x["score"], reverse=True)

                # Goes to the first position in the list.
                file.seek(0)

                # Puts 'data' in 'file'.
                json.dump(data, file, indent=4)
        
        # If no file found, creates new file.
        except FileNotFoundError:
            with open("scores.json", "w") as file:
                json.dump(data, file, indent=4)
    
    # Displays game messages to top of screen.
    def show_message(self, text):
        self.clear()
        self.write(text, False, align='center', font=('Arial', 20, 'normal'))
    
    # Puts the "High Scores" title above the list of high scores.
    def high_score_title(self):
        self.write('HIGH SCORES', False, align='left',
                   font=('Arial', 10, 'bold'))
