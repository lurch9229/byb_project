"""
Shows the highest number in a given list
"""


def biggest_value(num_list, index=0):  # Takes defined list as argument, and we set an index argument to value 0
    if index == len(num_list) - 1:  # Checks if the index is equal to the last index of the list
        return num_list[index]
    else:
        current_index = num_list[index]  # Get current and next indexes to calculate which of the 2 is bigger
        next_index = biggest_value(num_list, index+1)  # Recursion starts when biggest_value() is called
        return max(current_index, next_index)
        # Max() built-in is used to tidy "return current_index if current_index > next_index else next_index"


my_list = [1, 12, 5, 16, 12, 4]
highest_value = biggest_value(my_list)

print(f"The largest number in {my_list} is:\n{highest_value}")
