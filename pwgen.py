#####################################################################
#                        PASSWORD GENERATOR                         #
#####################################################################
# Author: Josh Stokes
# Date: 04 April 2024
# Purpose: Generate a random password
#####################################################################
import csv
import datetime
import os
import random

# Set constants.
DIR_PATH = os.path.dirname(__file__)
CSV_FILE = DIR_PATH + "\\pw.csv"

# Gets today's date.
today = datetime.date.today()

# List and final string for password.
password_list = []
password_string = ""

#-----------------------> Character Lists <-------------------------#
# Stores available characters.
upper_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
int_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spc_list = ['!', '@', '#', '$']
#-------------------------------------------------------------------#

# Function to check input for int less than 21.
# def check_input(user_input):
#     if user_input < 21:
#         print("--> Valid input.")
#     else:
#         print("--> Input value must be an integer of 20 or less.")

# Display intro messages.
print("\n--> Welcome to Josh's Random Password Generator.")
site = input("--> Site/Service: ")
user_name = input("--> Username: ")
pw_type = input("--> Manual Password OR Random Password? (M/R): ").upper()

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

# Create a Manual OR Random password.
if pw_type == "M":
    password_string = input("--> Manual Password: ")

elif pw_type == "R":
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
else:
    print("\n--> Invalid input. Please choose M or R.")
    password_string = "-----"

#-------------------------> Final Output <--------------------------#
print("\n---------------------------------------")
print(site)
print(f"Username: {user_name}")
print(f"Password: {password_string}")
print("---------------------------------------\n")
#-------------------------------------------------------------------#

#-----------------------> Add Data to CSV <-------------------------#
new_data = [site, user_name, password_string, today]

# Check if the CSV file exists
if os.path.exists(CSV_FILE):

    # If the file exists, open it in append mode
    with open(CSV_FILE, 'a', newline='') as file:

        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the new data to the CSV file
        writer.writerow(new_data)

    print("Data added to existing CSV file.")

else:

    # If the file does not exist, create it and write the data
    with open(CSV_FILE, 'w', newline='') as file:

        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header (if needed)
        writer.writerow(['Site', 'UserName', 'PassWord', 'Date'])

        # Write the new data to the CSV file
        writer.writerow(new_data)

    print("CSV file created and data added.")

#####################################################################
