# QUESTION 10: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again

# Then, the output should be:
# again and hello makes perfect practice world

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data.

input_value = input('Enter a sentence: ').split(' ')

SENTENCE = ''

for word in sorted(set(input_value)):
    SENTENCE += f'{word} '

print(SENTENCE)


# QUESTION 11: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# Example:
# 0100,0011,1010,1001

# Then the output should be:
# 1010

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

value = input('Enter comma seperated 4 digit binary numbers: ').split(',')

value = [int(num) for num in value]
print(value)

value = [num for num in value if (len(str(num)) == 4) and (num % 5 == 0)]

print(','.join(map(str, value)))


# QUESTION 12: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

nums = []

str_nums = [str(num) for num in range(1000, 3001)]

for num in str_nums:
    if (int(num[0]) % 2 == 0) and (int(num[1]) % 2 == 0) and (int(num[2]) % 2 == 0) and (int(num[3]) % 2 == 0):
        nums.append(num)

print(','.join(nums))


# QUESTION 13: Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:
# 

# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

import re

input_value = input('Enter: ')

letters = re.findall(r'[a-zA-Z]', input_value)
digits = re.findall(r'\d', input_value)

print(f'LETTERS: {len(letters)}')
print(f'DIGITS: {len(digits)}')


# ----------OR----------

# input_value = input('Enter: ')

# letters, digits = 0, 0

# for i in input_value:
#     if i.isalpha():
#         letters += 1
#     elif i.isnumeric():
#         digits += 1

# print(f'LETTERS: {letters}')
# print(f'DIGITS: {digits}')
