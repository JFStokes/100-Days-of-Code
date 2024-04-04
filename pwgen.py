#####################################################################
#                        PASSWORD GENERATOR                         #
#####################################################################
# Author: Josh Stokes
# Date: 04 April 2024
# Purpose: Generate a random password

#####################################################################
import random

# List and final string for password.
password_list = []
password_string = ""

# Stores available characters.
upper_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spc_list = ['!', '@', '#', '$', '%']

# Function to check input for int less than 21.
def check_input(user_input):
    if user_input < 21:
        print("--> Valid input.")
    else:
        print("--> Input value must be an integer of 20 or less.")

# Display intro messages.
print("--> Welcome to Josh's Random Password Generator.")
print("--> Enter the number of upper, lower, integers, and special characters.\n")

# Function to check for valid input and return random characters.
def process_input(user_input, list):
    try:
        user_input = int(user_input)
        print("--> Input accepted.")
    except:
        TypeError
        print("--> Input value must be an integer of 20 or less.")
    if list == "u":
        for num in range(user_input):
            choice = random.choice(upper_list)
            password_list.append(choice)
    elif list == 'l':
        pass
    elif list == 'i':
        pass
    elif list == 's':
        pass
    print(password_list)
        
num_of_characters = input("--> ")
process_input(num_of_characters, "u")

num_of_characters = input("--> ")
process_input(num_of_characters, "u")
        
    # check_input(upper_char)
    # selected_chars = random.choices(upper_list, k=upper_char)
    # password_list = selected_chars
    # print(password_list)

# try:
#     lower_char = int(input("--> Number of lowercase: "))
# except:
#     TypeError
#     print("--> Input value must be an integer of 20 or less.")
# check_input(lower_char)
# selected_chars = random.choices(lower_list, k=lower_char)
# password_list.append(selected_chars)
# print(password_list)


# try:
#     int_char = int(input("--> Number of integers: "))
# except:
#     TypeError
#     print("--> Input value must be an integer of 20 or less.")
# check_input(int_char)
# selected_chars = random.choices(int_list, k=int_char)
# password_list.append(selected_chars)
# print(password_list)


# try:
#     spc_char = int(input("--> Number of special characters: "))
# except:
#     TypeError
#     print("--> Input value must be an integer of 20 or less.")
# check_input(spc_char)
# selected_chars = random.choices(spc_list, k=spc_char)
# password_list.append(selected_chars)
# print(password_list)


# # Puts the characters in a random order and puts them into a string.
# random.shuffle(password_list)
# print(password_list)
# password_string = ', '.join(password_list)

# # Displays the final password.
# print(f'--> Your new password is: {password_string}')

#####################################################################
