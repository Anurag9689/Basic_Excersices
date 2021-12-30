# Question: 1
# Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiple(n, m):  # Defining the function which will find if n is some multiple of m of not!
    if not isinstance(n, (int, float)) and not isinstance(m, (int, float)):  # Checking for correct input (int, float)
        # print("Please Input correct arguments!")
        return "Please Input correct/Valid arguments: \n (Both n & m should be " \
               "integers or floating point numbers & in correct order \"is_multiple(n, m)\" (Where n = mi)" \
               " --> n is some multiple of m <-- !"  # Showing some correct output if something goes wrong
    elif n % m == 0 and isinstance(n, (int, float)) and isinstance(m, (int, float)):
        return True
    else:
        return False


print(is_multiple(45, 5))
print(is_multiple(45, 7))

