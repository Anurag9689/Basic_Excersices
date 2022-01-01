# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

the_list = [2**k for k in range(0, 9)]  # Using comprehension syntax & The expression 2**k
print(the_list)
