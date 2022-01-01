# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0,
# what is the equivalent index j ≥ 0 such that s[j] references
# the same element?
#  a  n  u  r  a  g
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1
#  0 = -n + j
#  k = -n + j
#  k + n = j
def equivalent_index(s):  # Making a function for finding a negative index which references
    # the same index as a positive index

    n = len(s)  # Python built-in function len(iterable) is used to find the length of the iterable

    # print([ch for ch in s])  # Making a list of each character in 's' string using a python comprehension syntax

    # print([(num, chr_1) for num, chr_1 in enumerate(s)])  # using enumerate(iterable) function to numerate
    # each item in the list

    print("(k  s[k])", "(j, s[j])")  # Just for some reference
    for k in range(-1, -n-1, -1):   # using a for loop with range(-1, -n-1, -1)
        j = k + n    # An expression is derived for j>=0 & -n <= k < 0
        print((k, s[k]), (j, s[j]))


equivalent_index("anurag_pandey")
