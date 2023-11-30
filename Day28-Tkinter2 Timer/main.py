import math
import os
import time
import tkinter
# ------------------------- CONSTANTS ----------------------------- #
DIR_PATH = os.path.dirname(__file__)
TOMATO_PATH = os.path.join(DIR_PATH, 'tomato.png')
print(f'The TOMATO_PATH is {TOMATO_PATH}')
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ------------------------ TIMER RESET ---------------------------- #

# ---------------------- TIMER MECHANISM -------------------------- #
def start_timer():
    count_down(5 * 60)

# -------------------- COUNTDOWN MECHANISM ------------------------ #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f'0{count_min}'
    
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    tomato_canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, count_down, count - 1)

# -------------------------- UI SETUP ----------------------------- #
# Create window.
window = tkinter.Tk()
window.title('Josh\'s Tomato Timer')
window.config(padx=100, pady=50, bg=YELLOW)

# Create tomato image/text.
tomato_canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file=TOMATO_PATH)
tomato_canvas.create_image(100, 112, image=tomato_image)
timer_text = tomato_canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
tomato_canvas.grid(column=1, row=1)

# Create 'Timer' label.
timer_label = tkinter.Label(font=(FONT_NAME, 35, 'bold'),
                            background=YELLOW, foreground=GREEN,
                            text='Timer', justify='center')
timer_label.grid(column=1, row=0)

# Creat Start button.
start_button = tkinter.Button(font=(FONT_NAME, 8, 'bold'),
                              text='Start', command=start_timer)
start_button.grid(column=0, row=2)

# Create Reset button.
reset_button = tkinter.Button(font=(FONT_NAME, 8, 'bold'),
                              text='Reset')
reset_button.grid(column=2, row=2)

# Create check mark label.
check_mark_label = tkinter.Label(font=(FONT_NAME, 10, 'bold'),
                                 background=YELLOW, foreground=GREEN,
                                 text='✔')
check_mark_label.grid(column=1, row=3)


# ----------------------------------------------------------------- #
window.mainloop()
