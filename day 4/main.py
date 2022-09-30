# Question 14:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

from functools import reduce


input_value = list(input('Enter a sentence: '))

UPPERCASE = 0
LOWERCASE = 0

for letter in input_value:
    if letter.isupper():
        UPPERCASE += 1
    elif letter.islower():
        LOWERCASE += 1

print(f'UPPER CASE {UPPERCASE}')
print(f'LOWER CASE {LOWERCASE}')


# Question 15:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program:

# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


number = input('Enter a number: ')

total = int(number) + int(number * 2) + int(number * 3) + int(number * 4)

print(total)


# ---------OR---------------

x = input('Enter a number: ')
reduce(lambda x, y: int(x) + int(y), [x*i for i in range(1, 5)])
