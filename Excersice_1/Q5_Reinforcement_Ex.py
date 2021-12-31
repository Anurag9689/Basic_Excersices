# Give a single command that computes the sum from
# Q4_Reinforcement_Ex, relying on Python’s comprehension syntax and the built-in sum function.

def sum_of_squares(n):  # Same as previous question, Finding the Sum of squares of first positive integers less than
    #  'n'
    total_sum = sum([k*k for k in range(0, n)])  # Using the python built-in function 'sum(any_iterable)' &
    # using the python's comprehension syntax to make a list quickly
    # 'any_expression' for 'some_counter' in range(starting_value, stopping_value+1)
    return total_sum


print(sum_of_squares(11))
