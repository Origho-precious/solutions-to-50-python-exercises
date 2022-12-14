'''
  DAY TWO
'''


# QUESTION 4: Write a program which accepts a sequence of comma-separated
# numbers from console and generate a list and a tuple which contains every
# number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to
# be a console input.tuple() method can convert list to tuple

# import re

input_value = input('Enter comma seperated numbers')

my_list = input_value.split(',')
# ---------------OR-------------------
# my_list = re.split(r',', input_value)

my_tuple = tuple(my_list)

print(my_list)
print(my_tuple)


# QUESTION 5: Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters

class PrintMachine():
    input_value = ''

    def __init__(self, value):
        self.input_value = value

    def getString(self):
        self.input_value = input('Enter anything')

    def printString(self):
        print(self.input_value.upper())


my_print_machine = PrintMachine('Hello!');

my_print_machine.getString()
my_print_machine.printString()


# QUESTION 6: Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a
# comma-separated sequence.For example Let us assume the following comma
# separated input sequence is given to the program:

# 100,150,180
# The output of the program should be:

# 18,22,24

# Hints:
# If the output received is in decimal form, it should be rounded off to its
# nearest value(for example, if the output received is 26.0, it should be
# printed as 26).In case of input data being supplied to the question, it
# should be assumed to be a console input.

import math

C = 50
H = 30


def calc(num):
    return math.sqrt((2 * C * num)/H)


D = input('Enter comma seperated numbers')
D = [int(item) for item in D.split(',')]

ans = [int(calc(num)) for num in D]


print(','.join(map(str, D)))


# QUESTION 7: Write a program that accepts a comma separated sequence of words
# as input and prints the words in a comma-separated sequence after sorting
# them alphabetically.

# Suppose the following input is supplied to the program:

# without,hello,bag,world
# Then, the output should be:

# bag,hello,without,world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


str_list = input('Enter comma seperated words').split(',')

print(','.join(sorted(str_list)))


# QUESTION 8: Write a program that accepts sequence of lines as input and prints
# the lines after making all characters in the sentence uppercased.

# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect

# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

sentences = []

while True:
    sentence = input('Enter multiline sentences: ')
    if sentence:
        sentences.append(sentence.upper())
    else:
        break

for sentence in sentences:
    print(sentence)
