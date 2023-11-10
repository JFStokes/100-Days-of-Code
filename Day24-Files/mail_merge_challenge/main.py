import os

# Set Constants.
CUR_DIR = os.getcwd()
IN_LTR_TXT = CUR_DIR + '\Day24-Files/mail_merge_challenge/Input/Letters/starting_letter.txt'
IN_NAMES_TXT = CUR_DIR + '\Day24-Files\mail_merge_challenge\Input/Names\invited_names.txt'
OUT_LETTERS_PATH = CUR_DIR + '\Day24-Files\mail_merge_challenge\Output\ReadyToSend'
print(f'---DEBUG: The READY TO SEND path is {OUT_LETTERS_PATH}')

starting_letter = ''

# Open 'starting_letter.txt'.
with open(IN_LTR_TXT) as letter:

    # Create a multi-line string with the letter.
    starting_letter = letter.read()

# Open 'invited_names.txt'.
with open(IN_NAMES_TXT) as names:

    # Create an array with the names.
    starting_names = names.readlines()

# Use a 'for' loop to add Names to the Letter.
for name in starting_names:

    # Replace '[name]' with a name from the 'starting_names' array.
    starting_letter = starting_letter.replace('[name],', name)

    # Trip the extra characters from the name to create a 'file_name'.
    file_name = name.strip(',\n')

    # Save letter as new file.
    with open(f'{OUT_LETTERS_PATH}\{file_name}.txt', mode='+a') as new_letter:
        new_letter.write(starting_letter)
    
    # Replace the name with '[name]' to prepare for the next name.
    starting_letter = starting_letter.replace(name, '[name],')
