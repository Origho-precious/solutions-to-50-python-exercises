'''
  DAY ONE
'''

# QUESTION 1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

# numbers = []

# for num in range(2000, 3201):
#     if num % 7 == 0 and num % 5 != 0:
#         numbers.append(str(num))


# # List comprehension
# num_list = [num for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]

# print(','.join(numbers))


# QUESTION 2: Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

# input_value = int(input('Enter number'))

# TOTAL = 1

# for num in range(1, input_value + 1):
#     TOTAL *= num

# print(TOTAL)


# QUESTION 3: With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

input_value = int(input('Enter number'))

my_dict = dict()

for i in range(1, input_value + 1):
    my_dict[i] = i * i


# object comprehension
my_dict = {i: i*i for i in range(1, input_value + 1)}

print(my_dict)
