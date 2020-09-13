def merge_sort(list_in):
    if len(list_in) == 0 or len(list_in) == 1:
        return list_in
    else:
        middle = len(list_in) // 2
        first_list = merge(list_in[:middle])
        second_list = merge(list_in[middle:])
        list_out = []
        index1 = 0
        index2 = 0
        while index1 < len(first_list) and index2 < len(second_list):
            if first_list[index1] < second_list[index2]:
                list_out.append(first_list[index1])
                index1 += 1
            else:
                list_out.append(second_list[index2])
                index2 += 1
        if index1 < len(first_list):
            list_out.extend(first_list[index1:])
        if index2 < len(second_list):
            list_out.extend(second_list[index2:])
    return list_out
