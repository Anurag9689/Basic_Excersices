# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd
# from typing import List, Any

import quick_sort_method as qs
sample_list = [33, 98, 52, 74, 18, 81, 70, 85, 81, 2, 11, 44, 81, 66, 81, 98, 48, 17, 55, 39, 72, 62, 69, 8, 29, 77,
               81, 3, 6, 70, 81, 60, 93, 29, 80, 92, 35, 15, 87, 57, 91, 85, 22, 37, 78, 8, 34, 44, 1, 78, 14, 52, 66,
               38, 36, 8, 17, 55, 83, 93, 53, 36, 76, 47, 92, 82, 47, 8, 78, 59, 27, 1, 39, 13, 36, 94, 10, 66, 36, 40,
               66, 45, 16, 82, 19, 33, 1, 54, 7, 80, 12, 1, 54, 33, 52, 24, 49, 7, 3, 5]


def odd_product_finder(sequence):
    odd_num_list = [odd_num for odd_num in sequence if odd_num % 2 == 1]
    qs.sort_it(odd_num_list)
    final_odd_list = [odd_num_list[final_odd_num_index] for final_odd_num_index in range(0, len(odd_num_list)-1)
                      if odd_num_list[final_odd_num_index] < odd_num_list[final_odd_num_index+1]]
    final_odd_list.append(odd_num_list[len(odd_num_list)-1])
    final_list = []
    for number_1 in final_odd_list:
        for number_2 in final_odd_list:
            if number_1 == number_2:
                continue
            final_list += [(number_1, number_2)]
    return final_list


print(odd_product_finder(sample_list))
