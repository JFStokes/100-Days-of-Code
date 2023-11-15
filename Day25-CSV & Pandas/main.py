#####################################################################
#                           CSV & Pandas                            #
#####################################################################
# import csv
import os
import pandas

# Get Current Working Directory.
CWD = os.getcwd() + '\\Day25-CSV & Pandas\\'

# Open the CSV file.
# with open(CWD + 'weather.csv') as data:

    # Reads each line of data as an item in a list.
    # data = data.readlines()

############### Strip string excess and add to list. ################
# data_list = []
# for line in data:

    # Strip '\n' from each line of data.
    # stripped_line = line.strip('\n')

    # Add the stripped line to the data list.
    # data_list.append(stripped_line)

########################## Use csv.reader ###########################
# with open(CWD + 'weather.csv') as data:
#     data = csv.reader(data)
#     temeratures = []
#     for row in data:
#         if row[1] != 'Temp':
#             temeratures.append(int(row[1]))

######################## Use Pandas read_csv ########################
data = pandas.read_csv(CWD + 'weather.csv')
print(data['Temp'])

#####################################################################