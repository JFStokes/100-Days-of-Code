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
site = input("--> Site/Service: ")
user_name = input("--> Username: ")

# Function to check for valid input and return random characters.
def process_input(user_input, list):
    try:
        user_input = int(user_input)
    except:
        TypeError
        print("--> Input value must be an integer of 20 or less.")
    if list == "u":
        for num in range(user_input):
            choice = random.choice(upper_list)
            password_list.append(choice)
    elif list == 'l':
        for num in range(user_input):
            choice = random.choice(lower_list)
            password_list.append(choice)
    elif list == 'i':
        for num in range(user_input):
            choice = random.choice(int_list)
            password_list.append(choice)
    elif list == 's':
        for num in range(user_input):
            choice = random.choice(spc_list)
            password_list.append(choice)
        
num_of_characters = input("--> Num of Uppercase: ")
process_input(num_of_characters, "u")

num_of_characters = input("--> Num of Lowercase: ")
process_input(num_of_characters, "l")

num_of_characters = input("--> Num of Integers: ")
process_input(num_of_characters, "i")

num_of_characters = input("--> Num of Special Characters: ")
process_input(num_of_characters, "s")

random.shuffle(password_list)

password_string = ''.join(password_list)

print(f"\n{site}")
print(f"Username: {user_name}")
print(f"Password: {password_string}\n")

#####################################################################
