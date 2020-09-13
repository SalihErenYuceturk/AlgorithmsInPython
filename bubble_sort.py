def bubble_sort(list_in):
    listOut = list_in[:]
    unsorted_index = len(listOut) - 1
    while unsorted_index > 0:
        sorted_index = 0
        index = 0
        while index < unsorted_index:
            if listOut[index] > listOut[index + 1]:
                listOut[index], listOut[index + 1] = listOut[index + 1], listOut[index]
                sorted_index = index
            index += 1
        unsorted_index = sorted_index
    return listOut
