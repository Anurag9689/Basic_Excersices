# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

# my_data = [1, 4, 8, 23, 87, 10, 24, 9, 17, 0, 9, -3, -2, -23, 4]


def minmax(my_data):  # Defining a function that will find the min and max in a given sequence
    max_num = 0       # Declaring our max number
    min_num = 0       # Declaring our min number
    for number in my_data:  # using a for loop for linear going over all the elements in the sequence
        if number >= max_num:  # Comparing for maximum value
            max_num = number    # if found higher value then capturing that value
        # elif item <= max_num:
        #     pass
        if number <= min_num:    # Comparing for minimum value
            min_num = number     # if found lower value then capturing that value
        # elif item >= min_num:
        #     pass
    minmax_tuple = (min_num, max_num)   # making at tuple of min & max values for returning
    return minmax_tuple  # Returning both values as the elements of the tuple


print(minmax((1, 4, 8, 23, 87, 10, 24, 9, 17, 0, 9, -3, -2, -23, 4)))
