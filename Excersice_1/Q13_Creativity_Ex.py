# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.


sample_list = [33, 98, 52, 74, 18, 81, 70, 85, 81, 2, 11, 44, 81, 66, 81, 98, 48, 17, 55, 39, 72, 62, 69, 8, 29, 77,
               81, 3, 6, 70, 81, 60, 93, 29, 80, 92, 35, 15, 87, 57, 91, 85, 22, 37, 78, 8, 34, 44, 1, 78, 14, 52, 66,
               38, 36, 8, 17, 55, 83, 93, 53, 36, 76, 47, 92, 82, 47, 8, 78, 59, 27, 1, 39, 13, 36, 94, 10, 66, 36, 40,
               66, 45, 16, 82, 19, 33, 1, 54, 7, 80, 12, 1, 54, 33, 52, 24, 49, 7, 3, 5]

sample_list_2 = sample_list.copy()


def reverse_it(iterable):
    n = len(iterable)
    for x in range(0, n // 2):
        iterable[n - 1 - x], iterable[x] = iterable[x], iterable[n - 1 - x]
    return iterable


print(reverse_it(sample_list))

sample_list_2.reverse()

if sample_list == sample_list_2:
    print(True)
