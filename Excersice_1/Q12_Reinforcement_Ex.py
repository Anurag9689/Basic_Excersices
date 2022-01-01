# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence.
# The random module includes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.

import random as rd  # Imported 'Random' module file as 'rd' for short-form
sample_list = []  # Declaring & initializing empty list
start = int(input("Enter the start number: "))  # Inputting a start number
stop = int(input("Enter the start number: "))  # Inputting a stop number
step = int(input("Enter the start number: "))  # Inputting a step number
for x in range(start, stop, step):   # using a for loop for looping through our randrange() function
    sample_list.append(rd.randrange(start, stop))   # appending new pseudo-randoms to sample_list

print(sample_list)   # printing a 'sample_list'
print(rd.choice(sample_list))  # using the choice function to randomly choose the element in sample_list
print(len(sample_list))
