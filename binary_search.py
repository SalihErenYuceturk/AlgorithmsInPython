def binary(ordered_list, search_value):
    maximum = len(ordered_list) - 1  # Initial maximum bound for the index.
    minimum = 0  # Initial minimum bound for the index.
    index = (maximum + minimum) // 2  # Middle point.
    while ordered_list[index] != search_value and minimum != maximum:
        if search_value < ordered_list[index]:
            maximum = index - 1
        if search_value > ordered_list[index]:
            minimum = index + 1
        index = (maximum + minimum) // 2
    if ordered_list[index] == search_value:
        return index
    elif minimum == search_value:
        return minimum
    elif ordered_list[index] != search_value:
        return -1
