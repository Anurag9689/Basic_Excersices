def sort_it(iterable):
    start = 0
    end = len(iterable) - 1

    def partition(a_list, start, end):
        pivot_index = start
        pivot_value = a_list[end]
        for i in range(start, end):
            if a_list[i] < pivot_value:
                swap(a_list, i, pivot_index)
                pivot_index += 1
        swap(a_list, pivot_index, end)
        # print(a_list)
        return pivot_index

    def swap(a_list, a, b):
        temp = a_list[a]
        a_list[a] = a_list[b]
        a_list[b] = temp

    def quick_sort_it(iterable, start, end):
        if start >= end:
            return
        index = partition(iterable, start, end)
        quick_sort_it(iterable, start, index - 1)
        quick_sort_it(iterable, index + 1, end)
    quick_sort_it(iterable, start, end)

    return iterable


# sample_list = [33, 98, 52, 74, 18, 81, 70, 85, 81, 2, 11, 44, 81, 66, 81, 98, 48, 17, 55, 39, 72, 62, 69, 8, 29, 77,
#                81, 3, 6, 70, 81, 60, 93, 29, 80, 92, 35, 15, 87, 57, 91, 85, 22, 37, 78, 8, 34, 44, 1, 78, 14, 52, 66,
#                38, 36, 8, 17, 55, 83, 93, 53, 36, 76, 47, 92, 82, 47, 8, 78, 59, 27, 1, 39, 13, 36, 94, 10, 66, 36,
#                40, 66, 45, 16, 82, 19, 33, 1, 54, 7, 80, 12, 1, 54, 33, 52, 24, 49, 7, 3, 5]
