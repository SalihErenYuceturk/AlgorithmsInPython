def remove_duplicates(list_in):
    list_out = []
    if len(list_in) != 0:
        fresh = list_in[0]
        index = 1
        while index < len(list_in):
            if list_in[index] != fresh:
                list_out.append(fresh)
                fresh = list_in[index]
            index += 1
        list_out.append(fresh)
    return list_out
