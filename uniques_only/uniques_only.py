def uniques_only(in_iter):
    tmp_lst = []
    for i, j in enumerate(in_iter):
        if j in tmp_lst:
            pass
        else:
            tmp_lst.append(j)
    return tmp_lst