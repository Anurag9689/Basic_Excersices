# Give a single command that computes the sum from
# Q6_Reinforcement_Ex, relying on Python’s comprehension syntax and the built-in sum function.

def sum_of_squares_of_odd(k):  # Finding the sum of squares of first odd natural number less than
    # argument 'k'
    total_sum = sum([n*n for n in range(1, k, 2)])  # Used python built-in sum() & Comprehension syntax for making
    # odd squares list less that 'k'
    return total_sum  # Returning total_sum


print(sum_of_squares_of_odd(3))
