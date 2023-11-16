#####################################################################
#                     SQUIRREL CENSUS WITH CSV                      #
#####################################################################
# Counts the number of red, gray, and black squirrels in the 2018
#   squirrel census in NYC's Central Park. Census data is stored in
#   the "2018_Squirrel_Data.csv" file. Results of the count will be
#   placed in the "squirrel_count.csv" file.
# Date: 15 November 2023
# Author: Josh Stokes
import pandas

# Read data from csv and create a dataframe.
data = pandas.read_csv('2018_Squirrel_Data.csv')

# Get fur color series from the dataframe and convert to a list.
fur_color_list = data['Primary Fur Color'].to_list()

# Count the number of each color inside the list.
gray_count = fur_color_list.count('Gray')
red_count = fur_color_list.count('Cinnamon')
black_count = fur_color_list.count('Black')

# Create a dict with the new data.
data_dict = {
    'Fur Color': ['gray', 'red', 'black'],
    'Count': [gray_count, red_count, black_count]
}

# Create a dataframe with the dict.
new_data = pandas.DataFrame(data_dict)
print(new_data)

# Create a csv file with the dataframe.
new_data.to_csv('squirrel_count.csv')

#####################################################################