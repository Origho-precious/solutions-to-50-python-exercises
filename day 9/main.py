# Question 26:
# Define a function which can compute the sum of two numbers.

# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

def add_num(num1, num2):
    return num1 + num2


print(add_num(2, 3))


# Question 27:
# Define a function that can convert a integer into a string and print it in console.

# Hints:
# Use str() to convert a number to string.

def to_string(num):
    print(str(num))


to_string(22)

# Question 28:
# Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

# Hints:
# Use int() to convert a string to integer.


def sum_str_nums(num1, num2):
    print(int(num1) + int(num2))


sum_str_nums('2', '4')


# Question 29:
# Define a function that can accept two strings as input and concatenate them and then print it in console.

# Hints:
# Use + sign to concatenate the strings.

def join_strings(str1, str2):
    print(str1 + str2)


join_strings('Hello ', 'there!')

# Question 30:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

# Hints:
# Use len() function to get the length of a string.


def print_string(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    else:
        print(str1)
        print(str2)


print_string('Hello', 'Hi')
print_string('Hello', 'Hi there')
print_string('Hello Li', 'Hi there')
