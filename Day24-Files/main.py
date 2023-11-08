#####################################################################
#                              FILES                                #
#####################################################################


######################## Opening & Reading ##########################
# Step 1: Open the file.
file = open('my_file.txt') 

# Step 2: Read the file.
contents = file.read()

# Step 3: Use the contents of the file.
print(contents)

# Step 4: Close the file.
file.close()

# Optimal & Preferred method.
with open('my_file.txt') as file2:
    contents2 = file2.read()
    print(f'Opened with alternate method: {contents2}')


############################# Writing ###############################
# Overides current data and writes new data (mode='w').
with open('my_file.txt', mode='w') as file3:
    file3.write('New text.')

# Adds to current data (mode='a').
with open('my_file.txt', mode='a') as file4:
    file4.write('\nAdded to New text.')

# Creates new file since 'new_file.txt' does not exist.
with open('new_file.txt', mode='a') as new_file:
    new_file.write('This is a new file.')
