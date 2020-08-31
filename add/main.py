def add(in_matrix_1, in_matrix_2):
    out_matrix = []
    for i in range(len(in_matrix_1)):
        row = []
        for j in range(len(in_matrix_1[i])):
            row.append(in_matrix_1[i][j] + in_matrix_2[i][j])
        out_matrix.append(row)
    return out_matrix