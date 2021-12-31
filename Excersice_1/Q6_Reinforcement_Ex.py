# Write a short Python function that takes a positive integer k and returns
# the sum of the squares of all the odd positive integers smaller than k.

# More Mathematical style for calculating sum
def sum_of_squares_odd(k):  # Defining a function for finding sum of squares of first odd number less than argument
    n = (k + 1) / 2   # 1**2 + 3**2 + 5**2 + ... + (2*n - 1)**2 -> so, k = 2*n - 1
    return (n*(2*n+1)*(2*n-1))/3 - k*k   # - k*k used for finding 'Smaller than k'

# More programmatic style for calculating sum
# def sum_of_squares_odd(n):
#     odd_sq_list = [k * k for k in range(1, n, 2)]
#     print(odd_sq_list)
#     total_sum = 0
#     for odd_sq_num in odd_sq_list:
#         total_sum += odd_sq_num
#     return total_sum


print(sum_of_squares_odd(11))
