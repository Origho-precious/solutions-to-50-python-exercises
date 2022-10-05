# Question 44:
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list. Use lambda to define anonymous functions.

square_nums = map(lambda num: num**2, range(1, 21))

print(list(square_nums))

# Question 45:
# Define a class named American which has a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.


class American:
    @staticmethod
    def print_nationality():
        print('American!')


American.print_nationality()

# Question 46:
# Define a class named American and its subclass NewYorker.

# Hints:
# Use class Subclass(ParentClass) to define a subclass.*


class NewYorker(American):

    @staticmethod
    def occupation():
        print('Software Engineering')
