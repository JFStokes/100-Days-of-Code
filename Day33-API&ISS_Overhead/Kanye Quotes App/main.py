from tkinter import *
import os
import requests

DIR = os.path.dirname(__file__)
BG_DIR = DIR + '\\background.png'
KANYE_DIR = DIR + '\\kanye.png'


def get_quote():
    response = requests.get(url='https://api.kanye.rest/')
    quote = response.json()["quote"]
    print(quote)
    canvas.itemconfig(quote_text, text=quote)

#-------------------------> Window Setup <--------------------------#
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BG_DIR)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text='', width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=KANYE_DIR)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()