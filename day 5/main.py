# Question 16:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. > Suppose the following input is supplied to the program:

# 1, 2, 3, 4, 5, 6, 7, 8, 9
# Then, the output should be:

# 1, 9, 25, 49, 81
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


numbers = input('Enter comma seperated numbers: ').split(',')

odd_numbers = [num for num in numbers if int(num) % 2 != 0]

print(','.join(odd_numbers))


# Question 17:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100
# Then, the output should be:

# 500
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


account_balance = 0

while True:
    log = input('Enter log entry: ')

    if not log:
        break

    if log.startswith('D'):
        account_balance += int(log.split(' ')[1])
    elif log.startswith('W'):
        account_balance -= int(log.split(' ')[1])


print(account_balance)
