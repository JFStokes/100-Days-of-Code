##################### DAY26-LIST COMPREHENSION ######################
import random
import pandas

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
# list_of_strings = input().split(',')
# list_of_int = [int(num) for num in list_of_strings]
# result = [num for num in list_of_int if num % 2 == 0]
# print(result)

# Returns dict of names with random scores.
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {student:random.randint(50, 100) for student in names}
# print(students_scores)

# Returns dict of names of students/scores who passed.
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {student:random.randint(50, 100) for student in names}
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 80}
# print(passed_students)

# Returns dict as a pandas dataframe
student_dict = {
    "student": ['Alex', 'Beth', 'Caroline'],
    "score": [70, 75, 80]
}
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)
student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)

for (index, row) in student_dataframe.iterrows():
    if row.score > 75:
        print(row)
