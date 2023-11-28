########################## DAY 27-TKINTER ###########################
import tkinter

# Create window object.
window = tkinter.Tk()

# Set the title of the window.
window.title('Josh\'s Window')

# Change configurations of the window.
window.config(background='black')

# Set the minimum size of the window.
window.minsize(width=500, height=300)

# Adds padding between widgets and window.
window.config(padx=50, pady=50)

# Create label object.
my_label = tkinter.Label(text='This is a Label',
                         font=('Consolas', 24, 'bold',), 
                         foreground='white', 
                         background='gray')

# Changes text of a previously created label.
my_label['text'] = 'This is a label (new)'

# Puts the label on the screen (default is center).
my_label.grid(column=0, row=0)

# Adds padding between label contents and label border.
my_label.config(padx=20, pady=20)

# Creates an entry object.
entry1 = tkinter.Entry(width=20, font=('Consolas', 12, 'normal'),
                       background='gray', foreground='white')
entry1.grid(column=3, row=2)
entry1.focus_set() # Gives entry1 focus when window loads.

# Creates a function to use in entry1 key binding.
def enter_in_entry1(event):
    my_label['text'] = entry1.get()
    entry1.delete(0, 'end')

# Creates a command for button1.
def clicked_button1():
    my_label['text'] = entry1.get()
    entry1.delete(0, 'end')

# Creates a button object.
button1 = tkinter.Button(text='Enter', 
                         background='gray',
                         font=('Consolas', 12, 'normal'),
                         command=clicked_button1)
button1.grid(column=1, row=1)

# Binds the <Enter> key to entry1.
entry1.bind('<Return>', enter_in_entry1)

new_button = tkinter.Button(text='new_button')
new_button.grid(column=2, row=0)

# Run built-in while loop (must be at end).
window.mainloop()
