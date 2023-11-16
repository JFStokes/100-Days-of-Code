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

# Reads the csv file into a variable (single line of code).
# data = pandas.read_csv(CWD + 'weather.csv')

# Gets the 'Temp' column.
# print(data['Temp'])

# Gets the type of data in the file (dataframe).
# print(type(data))

# Gets the type of data in the "Temp" column (series).
# print(type(data['Temp']))

# Sets data from a dataframe to a dict.
# data_dict = data.to_dict()
# print(data_dict)

# Sets "Temp" from series to a list.
# temp_list = data['Temp'].to_list()
# print(temp_list)

# Gets the average of the temp_list.
# average = sum(temp_list) / len(temp_list)
# average = round(average, 1)
# print(f'The average Temp is {average}')

# Alternate method for getting average using pandas method.
# print(data['Temp'].mean())

# Returns the largest number in a list.
# print(data['Temp'].max())

# Returns the row that == "Monday".
# print(data[data.Day == 'Monday'])

# Returns the row that contains the highest temp of the week.
# max_temp = data.Temp.max()
# print(data[data.Temp == max_temp])

# Returns the "Rain" for Monday.
# monday = data[data.Day == 'Monday']
# print(monday.Rain)

# Convert Monday's temp from F to C.
# monday = data[data.Day == 'Monday']
# monday_temp = monday.Temp
# monday_temp_c = (monday_temp - 32) * 5/9
# print(monday_temp_c)

# Create a dataframe from scratch.
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv(CWD + 'new_data.csv')


#####################################################################