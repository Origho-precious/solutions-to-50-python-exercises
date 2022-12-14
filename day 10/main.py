# Question 31:
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.

def create_dict():
    print({num: num**2 for num in range(1, 21)})


create_dict()


# Question 32:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

def print_dict_keys():
    my_dict = {num: num**2 for num in range(1, 21)}

    for item in list(my_dict.keys()):
        print(item)


print_dict_keys()


# Question 33:
# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.

def gen_list():
    numbers = [num**2 for num in range(1, 21)]
    print(numbers)


gen_list()


# Question 34:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use[n1:n2] to slice a list

def gen_list2():
    numbers = [num**2 for num in range(1, 21)]
    print(numbers[0:5])


gen_list2()


# Question 35:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use[n1:n2] to slice a list

def gen_list3():
    numbers = [num**2 for num in range(1, 21)]
    print(numbers[-5:])


gen_list3()


# Question 36:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

# Hints: Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use[n1:n2] to slice a list

def gen_list4():
    numbers = [num**2 for num in range(1, 21)]
    print(numbers[:5])


gen_list4()

# Question 37:
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use tuple() to get a tuple from a list.


def gen_list5():
    numbers = [num**2 for num in range(1, 21)]
    numbers = tuple(numbers)

    print(numbers)


gen_list5()
