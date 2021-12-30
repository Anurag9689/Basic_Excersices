# Question 4
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(n):  # Defining a function which will make a list of squares of natural numbers less than argument
    # number 'n' & Add them all together
    num_list = [k*k for k in range(1, n)]  # making a list of squares of natural number less than 'n'
    print(num_list)   # Printing the list
    total_sum = 0   # declaring & initiating a variable which will store total sum
    for each_number in num_list:  # loop which will sum each element one by one
        total_sum += each_number  # expression to sum the numbers
    return total_sum  # Returning the total_sum


print(sum_of_squares(11))
