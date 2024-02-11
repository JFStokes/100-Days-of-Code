#####################################################################
#                         BIRTHDAY WISHER                           #
#####################################################################
# Uses data from csv to determine when a birthday exists and what the
#   person's email is. Then generates 1 of 3 email messages that 
#   wishes them a happy bday and emails it to them.
import datetime as dt
import os
import pandas as pd
import random
import smtplib

# Set CONSTANTS.
DIR_PATH = os.path.dirname(__file__)
CSV_FILE = DIR_PATH + '\\birthdays.csv'
LETTER_PATH = DIR_PATH + '\\letter_templates'

# Set global VARIABLES.
cur_dt = dt.datetime.now()
cur_mon = cur_dt.month
cur_day = cur_dt.day
today_is_bd = False
bd_kid = ''
bd_email = ''
bd_letter = ''
my_email = 'joshua.f.stokes.mil@gmail.com'
my_email_pw = 'cgfhzcjcgcazjvoo'


#----------------------> Check csv for bday <-----------------------#
# Get data from csv file & convert into dict/lists.
data = pd.read_csv(CSV_FILE)
data_dict = data.to_dict()
csv_mons = data['month'].to_list()
csv_days = data['day'].to_list()

# Checks months/days from data.
for mon in csv_mons:
    if mon == cur_mon:
        for day in csv_days:
            if day == cur_day:

                # Today is a bday! Gets name and email.
                today_is_bd = True
                for key, value in data['day'].items():
                    if value == day:
                        bd_kid = data['name'][key]
                        bd_email = data['email'][key]


#--------------------> Generate Random Letter <---------------------#
if today_is_bd:
    print(f'--> It is {bd_kid}\'s birthday! Email them at {bd_email}.')

    # Get a random letter.
    ran_num = random.randint(1, 3)
    bd_letter = LETTER_PATH + f'\\letter_{ran_num}.txt'

    # Adds name to the letter.
    with open(bd_letter) as letter_file:
        contents = letter_file.read()
        edited_contents = contents.replace('[NAME]', bd_kid)
else:
    print('--> Nobody has a birthday today.')


#-----------------------> Email the Letter <------------------------#
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    print('--> TLS connection complete. Logging into account.')
    connection.login(user=my_email, password=my_email_pw)
    print('--> Login successful. Sending email.')
    connection.sendmail(
        from_addr=my_email,
        to_addrs=bd_email,
        msg=f'Subject: HAPPY BIRTHDAY!!!\n\n{edited_contents}'
    )
    print('--> Email Sent.')


#-------------------------------------------------------------------#
    