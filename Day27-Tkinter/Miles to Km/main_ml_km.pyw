######################### MILES TO KM APP ###########################
# A GUI app to convert miles to kilometers.
import datetime
# import logging
import os
import pygame
from tkinter import *

# Get file path.
DIR_PATH = os.path.dirname(__file__)

# Setup logging.
# sys.stdout = open('output.log', 'a')
# sys.stderr = open('error.log', 'a')
# logging.basicConfig(filename='output.log', level=logging.NOTSET)
# logging.info(f'{now} Initiated')
def log(message):
    # with open('output.txt', mode='a') as file:
    #     file.write(f'\n{datetime.datetime.now()} {message}')
    print(message)
log('initiated 4.')

# Load image, icon, and ping sound.
pygame.mixer.init()
pygame.mixer.music.load(DIR_PATH + '/ping.mp3')
image_path = DIR_PATH + "/miles_to_km.png"
icon_path = DIR_PATH + "/miles_to_km.ico"

# Create the Window object.
window = Tk()
window.title('Josh\'s Miles to Km Converter')
window.config(background='black', width=500, height=500,
              padx=50, pady=50)
title_icon = PhotoImage(file=image_path)
window.iconphoto(True, title_icon)

# Create the miles entry.
miles_entry = Entry(font=('Consolas', 12, 'bold'),
                    background='gray', foreground='white',
                    width=10, justify='center',)
miles_entry.grid(column=2, row=1)
miles_entry.focus_set()

# Create the miles label.
miles_label = Label(font=('Consolas', 12, 'normal'),
                    background='black', foreground='white',
                    text='miles')
miles_label.grid(column=3, row=1)

# Create the km labels.
equal_to_label = Label(font=('Consolas', 12, 'normal'),
                       background='black', foreground='white',
                       text='is equal to', justify='right')
equal_to_label.grid(column=1, row=2)

km_num_label = Label(font=('Consolas', 12, 'bold'),
                 background='black', foreground='white',
                 text='---')
km_num_label.grid(column=2, row=2)

km_label = Label(font=('Consolas', 12, 'normal'),
                 background='black', foreground='white',
                 text='Km')
km_label.grid(column=3, row=2)


# Create the command for the button.
def calculate_clicked():
    pygame.mixer.music.play()
    # logging.info(f'{datetime.datetime.now()} calulated {miles_entry.get()} miles.')
    miles = miles_entry.get()
    km = float(miles) * 1.60934
    km_num_label['text'] = km


# Create the calculate button.
calculate_button = Button(font=('Consolas', 12, 'normal'),
                          background='gray', foreground='white',
                          text='Calculate',
                          command=calculate_clicked)
calculate_button.grid(column=2, row=3)

# Create command for entry binded key.
def enter_pressed(event):
    pygame.mixer.music.play()
    # logging.info(f'{datetime.datetime.now()} calulated {miles_entry.get()} miles.')
    miles = miles_entry.get()
    km = float(miles) * 1.60934
    km_num_label['text'] = km


# Bind key and command to entry.
miles_entry.bind('<Return>', enter_pressed)

# Add logo image.
photo = PhotoImage(file=image_path)
photo_label = Label(image=photo, justify='left')
photo_label.grid(column=0, row=0)


window.mainloop()
