def linear(list_in, search_value):
    index = 0
    while index < len(list_in) and list_in[index] != search_value:
        index = index + 1
        if list_in[index - 1] > search_value:
            return str("does not occur")
    if index == len(list_in):
        return str("does not occur")
    else:
        return index
