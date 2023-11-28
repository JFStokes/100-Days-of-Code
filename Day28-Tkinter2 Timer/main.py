import tkinter
# ------------------------- CONSTANTS ----------------------------- #
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

# -------------------- COUNTDOWN MECHANISM ------------------------ #

# -------------------------- UI SETUP ----------------------------- #
window = tkinter.Tk()
window.title('Josh\'s Tomato Timer')
window.config(padx=100, pady=50)

tomato_canvas = tkinter.Canvas(width=200, height=224)
tomato_image = tkinter.PhotoImage(file='"C:\\Users\\User\\Desktop\\Dev\\100 Days of Code\\Day28-Tkinter2 Timer\\tomato.png"')
tomato_canvas.create_image(103, 112, tomato_image)
tomato_canvas.create_text(103, 130)


window.mainloop()
