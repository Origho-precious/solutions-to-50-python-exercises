# The extended part of the repository starts from this page. Previous 94 problems were collected from the repository mentioned in intro. The following problems are collected from Hackerrank and other resources from internet.All the given solutions are in python 3.


# ----------------------------------------------------------------------------


# Question 95:
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# If the following string is given as input to the program:
# 5
# 2 3 6 6 5

# Then, the output of the program should be:
# 5

# Hints:
# Make the scores unique and then find 2nd best number


# Question 96:
# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

# If the following string is given as input to the program:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Then, the output of the program should be:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

# Hints:
# Use wrap function of textwrap module


# Question
# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

#     #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# Hints
# First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.


# Question 98:
# You are given a date. Your task is to find what the day is on that date.

# Input

# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

# 08 05 2015
# Output

# Output the correct day in capital letters.
# WEDNESDAY

# Hints:
# Use weekday function of calender module


# Question 99:
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input

# The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.

# 4
# 2 4 5 9
# 4
# 2 4 11 12
# Output

# Output the symmetric difference integers in ascending order, one per line.

# 5
# 9
# 11
# 12

# Hints:
# Use '^' to make symmetric difference operation.
