#####################################################################
#                          FLASH CARD APP                           #
#####################################################################
import os
import pandas
import random
import tkinter

# Gets path to this file and sets CWD.
DIR_PATH = os.path.dirname(__file__)
os.chdir(DIR_PATH) # Sets CWD.

#--------------------------> CONSTANTS <----------------------------#
FONT = 'Arial'
BACKGROUND_COLOR = "#B1DDC6"
WHITE = '#FFFFFF'
DATA_PATH = DIR_PATH + '\\data\\french_words.csv'
CARD_FRONT_PATH = DIR_PATH + '\\images\\card_front.png'
CARD_BACK_PATH = DIR_PATH + '\\images\\card_back.png'
RIGHT_PATH = DIR_PATH + '\\images\\right.png'
WRONG_PATH = DIR_PATH + '\\images\\wrong.png'

#--------------------------> FLIP CARD <----------------------------#
current_card = {}

def flip_card():
    card_image.config(file=CARD_BACK_PATH)
    card_canvas.itemconfig(top_label, text='English')
    card_canvas.itemconfig(bottom_label, text=current_card['English'])

#-----------------------> BUTTON COMMANDS <-------------------------#
data = pandas.read_csv(DIR_PATH + '/data/words_to_learn.csv')
data_dict = data.to_dict(orient='records')

def get_next_question():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    card_image.config(file=CARD_FRONT_PATH)
    card_canvas.itemconfig(top_label, text='French')
    current_card = random.choice(data_dict)
    card_canvas.itemconfig(bottom_label, text=current_card['French'])
    flip_timer = window.after(3000, flip_card)

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv('data/words_to_learn.csv')
    get_next_question()

#---------------------------> UI SETUP <----------------------------#
window = tkinter.Tk()
window.title('Josh\'s Flash Cards')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Create card canvas.
card_canvas = tkinter.Canvas(window, width=800, height=600,
                                   bg=BACKGROUND_COLOR,
                                   highlightbackground=BACKGROUND_COLOR)
card_image = tkinter.PhotoImage(file=CARD_FRONT_PATH)
card_canvas.create_image(400, 300, image=card_image)
card_canvas.grid(column=0, row=0, columnspan=2)

# Top Label.
top_label = card_canvas.create_text(400, 150, font=(FONT, 40, 'italic'),
                          text='', justify='center')

# Bottom Label.
bottom_label = card_canvas.create_text(400, 300, font=(FONT, 60, 'bold'),
                              text='', justify='center')

# Create wrong_button.
wrong_image = tkinter.PhotoImage(file=WRONG_PATH)
wrong_button = tkinter.Button(image=wrong_image, borderwidth=0,
                              padx=50, pady=50,
                              background=BACKGROUND_COLOR,
                              command=get_next_question)
wrong_button.grid(column=0, row=1)

# Create right_button.
right_image = tkinter.PhotoImage(file=RIGHT_PATH)
right_button = tkinter.Button(image=right_image, borderwidth=0,
                              padx=50, pady=50,
                              background=BACKGROUND_COLOR,
                              command=is_known)
right_button.grid(column=1, row=1)

#-------------------------------------------------------------------#
get_next_question()
window.mainloop()
