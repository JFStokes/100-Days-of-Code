####################### DAY26-NATO ALPHABET #########################
import pandas

# Load csv file.
csv_data = pandas.read_csv('Day26-NATO Alphabet/NATO Alphabet/nato_phonetic_alphabet.csv')

# Create dict from csv data (long version).
# data_dict = {letter:code for (letter, code) in csv_data.items()}
# letter_list = data_dict['letter'].to_list()
# code_list = data_dict['code'].to_list()
# nato_dict = {key: value for key, value in zip(letter_list, code_list)}

# Create dict from csv data (short version).
nato_dict = {row.letter: row.code for (index, row) in csv_data.iterrows()}

# Get user input.
user_name = input('Enter your name: ').upper()

# Create list of letters from user name.
name_list = [letter for letter in user_name]

# Return list of NATO Alphabet words.
nato_code = [nato_dict[word] for word in name_list if word in nato_dict]

# Print results.
print(nato_code)
