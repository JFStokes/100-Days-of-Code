##################### DAY26-LIST COMPREHENSION ######################

# Add 1 to each number in a list.
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# Take letters from a name and make list of numbers.
# name = 'Josh'
# new_list = [letter for letter in name]
# print(new_list)

# Multiply numbers in a range by 2.
# num_list = [num * 2 for num in range(1, 5)]
# print(num_list)

# Return list of names that have 4 char or less.
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# Return list of names that have 5 char or more and make them upper.
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# Squaring (a number multiplied by itself) numbers in a list.
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# print(squared_numbers)

# Return a list of even number from a list of numbers.
list_of_strings = input().split(',')
list_of_int = [int(num) for num in list_of_strings]
result = [num for num in list_of_int if num % 2 == 0]
print(result)