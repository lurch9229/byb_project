def merge(items, sections):
    # Unpack the start and end indices of the two sections to be merged
    i1_start, i1_end = sections[0]
    i2_start, i2_end = sections[1]

    # Initialize an empty list to hold the merged items
    merged_items = []

    # Initialize pointers for both sections
    i1 = i1_start
    i2 = i2_start

    # Merge the two sections by comparing the lengths of the items
    while i1 < i1_end and i2 < i2_end:
        if len(items[i1]) >= len(items[i2]):
            merged_items.append(items[i1])
            i1 += 1
        else:
            merged_items.append(items[i2])
            i2 += 1

    # Append any remaining items from both sections
    merged_items.extend(items[i1:i1_end])
    merged_items.extend(items[i2:i2_end])

    # Replace the original items with the merged items
    items[i1_start:i2_end] = merged_items


def merge_sort(items):
    n = len(items)
    subsection_size = 1

    # Continue merging sections until the subsection size exceeds the list length
    while subsection_size < n:
        for i in range(0, n, subsection_size * 2):
            # Determine the start and end indices of the two sections to be merged
            i1_start, i1_end = i, min(i + subsection_size, n)
            i2_start, i2_end = i1_end, min(i1_end + subsection_size, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)

            # Merge the sections
            merge(items, sections)

        # Double the subsection size for the next iteration
        subsection_size *= 2

    return items


strings = ["Hello, this is a test", "I like apples", "Sushi is better when it is fresh"]
sorted_strings = merge_sort(strings)
print(sorted_strings)
