def print_matrix_integer(matrix=[[]]):
    if not matrix:
        pass
    else:
        arr = ''
        for i in matrix:
            for j in i:
                if j == i[-1]:
                    print("{:d}".format(j), end="")
                else:
                    print("{:d}".format(j), end=" ")
            print()
