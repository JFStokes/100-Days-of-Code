import random
import os
import pyperclip
import tkinter
from tkinter import messagebox

# Gets path to this file.
DIR_PATH = os.path.dirname(__file__)

# Sets CWD.
os.chdir(DIR_PATH)
print(f'Script: CWD set to {DIR_PATH}')

# Sets path to logo.png.
LOCK_IMAGE_PATH = os.path.join(DIR_PATH, 'logo.png')

# Other Constants.
FONT = 'Consolas'

# --------------------- PASSWORD GENERATOR ------------------------ #
def generate_password():

    # Erase the password entry field.
    password_entry.delete(0, tkinter.END)

    # Lists with available letters, numbers, and symbols.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Create ranges for letters, numbers, and symbols.
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # A temporary password character list.
    password_list = []

    # Add characters to password list.
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    # Shuffle characters inside the password list.
    random.shuffle(password_list)

    # Join password characters together.
    password = ''.join(password_list)

    # Inserts password to entry and saves to clipboard.
    password_entry.insert(0, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")

# ----------------------- SAVE PASSWORD --------------------------- #
def save_to_txt():

    # Create variables by getting input from entries. 
    website_txt = website_entry.get()
    email_username_txt = email_username_entry.get()
    password_txt = password_entry.get()

    # Check for empty website entry.
    if website_txt == '':
        messagebox.showerror(title='Missing information',
                             message='Website is required.')
        return
    
    # Check for empty email/username entry.
    if email_username_txt == '':
        messagebox.showerror(title='Missing information',
                             message='Email/Username is required.')
        return
    
    # Check for empty password entry.
    if password_txt == '':
        messagebox.showerror(title='Missing information',
                             message='Password is required.')
        return

    # Create messagebox to confirm entries.
    is_ok = messagebox.askokcancel(title=website_txt,
                           message=f'These are the details entered:\
    \nEmail: {email_username_txt}\
    \nPassword: {password_txt}\
    \nIs this OK?')

    # If user clicks OK, save data and clear fields.
    if is_ok:
        # Save variable values to file.
        with open('data.txt', 'a') as file:
            file.write(website_txt + ' | ')
            file.write(email_username_txt + ' | ')
            file.write(password_txt + '\n')
        
        # Erase entry fields after saving.
        website_entry.delete(0, tkinter.END)
        email_username_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)

        # Set focus to the website entry.
        website_entry.focus()

# -------------------------- UI SETUP ----------------------------- #
window = tkinter.Tk()
window.title('Josh\'s Password Manager')
window.config(padx=50, pady=50)

# Create lock background image.
lock_canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file=LOCK_IMAGE_PATH)
lock_canvas.create_image(100, 100, image=lock_image)
lock_canvas.grid(column=1, row=0)

# Website Label.
website_label = tkinter.Label(font=(FONT, 12, 'normal'),
                              text='Website:', justify='center')
website_label.grid(column=0, row=1)

# Website Entry.
website_entry = tkinter.Entry(font=(FONT, 12, 'normal'),
                              width=35, justify='left')
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username Label.
email_username_label = tkinter.Label(font=(FONT, 12, 'normal'),
                                     text='Email/Username:', justify='center')
email_username_label.grid(column=0, row=2)

# Email/Username Entry.
email_username_entry = tkinter.Entry(font=(FONT, 12, 'normal'),
                                     width=35, justify='left')
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, 'joshua.stokes1617@yahoo.com')

# Password Label.
password_label = tkinter.Label(font=(FONT, 12, 'normal'),
                               text='Password:', justify='center')
password_label.grid(column=0, row=3)

# Password Entry.
password_entry = tkinter.Entry(font=(FONT, 12, 'normal'),
                               width=21, justify='left')
password_entry.grid(column=1, row=3)

# Generate Password Button.
generate_button = tkinter.Button(font=(FONT, 10, 'normal'),
                                 text='Generate Password',
                                 command=generate_password)
generate_button.grid(column=2, row=3)

# Add Button.
add_button = tkinter.Button(font=(FONT, 12, 'normal'),
                            text='Add', width=36, command=save_to_txt)
add_button.grid(column=1, row=4, columnspan=2)

# ----------------------------------------------------------------- #
window.mainloop()