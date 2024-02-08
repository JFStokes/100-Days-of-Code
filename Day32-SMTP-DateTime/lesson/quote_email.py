#####################################################################
#                           QUOTE EMAIL                             #
#####################################################################
# Description: Emails a random quote on a specific day of the month.
import datetime as dt
import os
import random
import smtplib


#-----------------------> GLOBAL VARIABLES <------------------------#
# Gets path to this file and setd CWD.
DIR_PATH = os.path.dirname(__file__)
os.chdir(DIR_PATH) # Sets CWD.

# Gets path to quotes file.
QUOTE_FILE = DIR_PATH + '\\quotes.txt'

# Time to send email.
time_to_send_email = 21

# Email Variables.
my_email = 'joshua.f.stokes.mil@gmail.com'
password = 'cgfhzcjcgcazjvoo'
to_email = 'macyhartel3@yahoo.com'

#---------------------------> GET DATE <----------------------------#
now = dt.datetime.now() # Gets current datetime.

#---------------------------> GET QUOTE <---------------------------#
# Opens the quotes file and makes a list of quotes.
with open(QUOTE_FILE) as q:
    quotes = q.readlines()

# Gets a random number within the quotes list.
ran_num = random.randint(0, len(quotes)) # Could also use random.choice(quotes).

# Stores the chosen quote.
quote = quotes[ran_num]


#--------------------------> SEND EMAIL <---------------------------#
if now.hour < time_to_send_email:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f'Subject:Motivation from Josh\n\n{quote}'
        )
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='joshua.stokes1617@yahoo.com',
            msg=f'Subject:Motivation from Josh\n\n{quote}'
        ) 

#####################################################################
