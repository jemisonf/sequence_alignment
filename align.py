def print_matrix(matrix):
    for row in matrix:
        for index in row:
            print (f"{index} ", end="")
        print("\n", end="")

def diff(char_i, char_j):
    return 10

def align(seq_1, seq_2):
    D = [[ 0 for j in range(len(seq_2) + 1)] for i in range(len(seq_1) + 1)]
    ptr = [[ 0 for j in range(len(seq_2) + 1)] for i in range(len(seq_1) + 1)]
    # 0 = LEFT
    # 1 = DOWN
    # 2 = DIAG
    print(D)
    for i in range(len(seq_1) + 1):
         D[i][0] = i
    for j in range(len(seq_2) + 1):
         D[0][j] = j

    for i in range(1, len(seq_1) + 1):
        for j in range(1, len(seq_2) + 1):
            D[i][j] = min(
                            D[i - 1][j] + 1,
                            D[i][j - 1] + 1,
                            D[i - 1][j - 1] + diff(seq_1[i - 1], seq_2[j - 1])
            )
            if (D[i - 1][j] + 1 < D[i][j - 1] + 1 and 
                D[i - 1][j] + 1 < D[i - 1][j - 1] + diff(seq_1[i - 1], seq_2[j - 1])):
                ptr[i][j] = 0
            if (D[i][j - 1] + 1 < D[i - 1][j] + 1 and 
                D[i][j - 1] + 1 < D[i - 1][j - 1] + diff(seq_1[i - 1], seq_2[j - 1])):
                ptr[i][j] = 1
            else:
                ptr[i][j] = 2
    return D[len(seq_1)][len(seq_2)], ptr


n, D = align("ata", "atga")
print(n)
print_matrix(D)
