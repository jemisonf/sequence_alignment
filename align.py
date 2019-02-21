from utils import AlignmentUtils

# test function please ignore -- will delete in final
def print_matrix(matrix):
    for row in matrix:
        for index in row:
            print (f"{index} ", end="")
        print("\n", end="")

class Aligner:
    def __init__(self, cost_filename='imp2cost.txt'):
        self.utils = AlignmentUtils(cost_filename)
        self.D = []

    def diff(self, char_i, char_j):
        return self.utils.get_cost(char_i, char_j)

    def deletion(self, i, j):
        return self.D[i - 1][j] + 1

    def insertion(self, i, j):
        return self.D[i][j - 1] + 1

    def alignment(self, i, j, seq_1, seq_2):
        return self.D[i - 1][j - 1] + self.diff(seq_1[i - 1], seq_2[j - 1])

    def align(self, seq_1, seq_2):
        self.D = [[ 0 for j in range(len(seq_2) + 1)] for i in range(len(seq_1) + 1)]
        ptr = [[ 0 for j in range(len(seq_2) + 1)] for i in range(len(seq_1) + 1)]
        # 0 = DOWN
        # 1 = LEFT
        # 2 = DIAG
        for i in range(len(seq_1) + 1):
            self.D[i][0] = i
        for j in range(len(seq_2) + 1):
            self.D[0][j] = j

        for i in range(1, len(seq_1) + 1):
            for j in range(1, len(seq_2) + 1):
                self.D[i][j] = min(
                                self.deletion(i, j),
                                self.insertion(i, j),
                                self.alignment(i, j, seq_1, seq_2)
                )
                if (self.deletion(i, j) < self.insertion(i, j) and self.deletion(i, j) < self.alignment(i, j, seq_1, seq_2)):
                    ptr[i][j] = 0
                if (self.insertion(i, j) < self.deletion(i, j) and self.insertion(i, j) < self.alignment(i, j, seq_1, seq_2)):
                    ptr[i][j] = 1
                else:
                    ptr[i][j] = 2
        return self.D[len(seq_1)][len(seq_2)], ptr


# aligner = Aligner()
# n, D = aligner.align("ATCC", "TCAC")
# print(n)
# print_matrix(D)
