# Question 21:
# A robot moves in a plane starting from the original point(0, 0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Here distance indicates to euclidean distance.
# Import math module to use sqrt function.

import math

directions = []

while True:
    input_value = input(
        'Enter direction and number of steps e.g UP 2: ').split(' ')

    if len(input_value) == 2:
        directions.append(tuple(input_value))
    else:
        break


a, b = 0, 0

for direction in directions:
    if direction[0] == 'RIGHT':
        a += int(direction[1])
    if direction[0] == 'LEFT':
        a -= int(direction[1])
    if direction[0] == 'UP':
        b += int(direction[1])
    if direction[0] == 'DOWN':
        b -= int(direction[1])

a = math.pow(a, 2)
b = math.pow(b, 2)

c = math.sqrt(abs(a - b))

print(math.ceil(c))
