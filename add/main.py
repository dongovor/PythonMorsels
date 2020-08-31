#add project
'''
def add(in_matrix_1, in_matrix_2):
    out_matrix = []
    for i in range(len(in_matrix_1)):
        row = []
        for j in range(len(in_matrix_1[i])):
            row.append(in_matrix_1[i][j] + in_matrix_2[i][j])
        out_matrix.append(row)
    return out_matrix
'''
def add(*in_args):
    for i in (*in_args):
        print('-----')
        print(i)
        print('-----')
    return 


in_1 = [[1, -2], [-3, 4]]
in_2 = [[2, -1], [0, -1]]

print(add(in_1, in_2))

in_1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
in_2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]

print(add(in_1, in_2))
