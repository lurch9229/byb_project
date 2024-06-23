my_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# We could sort the list first, then search for the number 9 using a binary search
# Linear search can be used to search without sorting the list but would be a higher Order complexity


def linear_search(lst,target):
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1


def insertion_sort(lst):
    for i in range(lst):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


def bin_search(lst, target):
    l = 0
    r = len(lst) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if lst[mid] == target:
            return mid
        elif lst < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


target_num = 9

print(f"Unsorted Array: {my_list}")

linear_index = linear_search(my_list, target_num)

if linear_index != -1:
    print(f"The target number of {target_num} is located at index {linear_index} using linear Search")
else:
    print(f"Target number not found in list using linear search")

insertion_sort(my_list)
print(f"Sorted List: {my_list}")

bin_index = bin_search(my_list, target_num)

if bin_index != -1:
    print(f"The target number of {target_num} can be found at index {bin_index} using Binary Search")