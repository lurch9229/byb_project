"""
Calculates the sum of a given list up to a defined index within the list
"""


def get_sum(num_list, index):  # Takes the defined list and index as args
    if index < 0:
        return 0  # This is to prevent an IndexError

    elif index >= len(num_list):
        sum(num_list)  # Sum() built-in is used to tidy "return get_sum(num_list, len(num_list) - 1)"

    else:
        return num_list[index] + get_sum(num_list, index - 1)  # Recursive starts when get_sum() is called


my_list = [1, 4, 5, 3, 12, 16]
defined_index = 4

print(f"Inputted list:\n{my_list}"
      f"\nThe result of the first {defined_index + 1} numbers added together are:"
      f"\n{get_sum(my_list, defined_index)}")
