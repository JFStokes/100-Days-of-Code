import datetime as dt

now = dt.datetime.now() # Gets current datetime.
year = now.year # Gets current year.
mon = now.month 

# Create a new datetime object.
date_of_birth = dt.datetime(year= 1988, month= 6, day= 26, hour=21)

print(date_of_birth)