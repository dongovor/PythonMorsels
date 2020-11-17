def compact(in_list):
    out_list = []
    for i in in_list:
        if i not in out_list:
            out_list.append(i)
        else:
            pass
    return out_list
