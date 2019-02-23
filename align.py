from utils import AlignmentUtils

class Aligner:
    def __init__(self, cost_filename='imp2cost.txt'):
        self.utils = AlignmentUtils(cost_filename)
        self.D = []

    def diff(self, char_i, char_j):
        return self.utils.get_cost(char_i, char_j)

    def deletion(self, i, j, seq_1, seq_2):
        return self.D[i - 1][j] + self.diff(seq_1[i - 1], '-')

    def insertion(self, i, j, seq_1, seq_2):
        return self.D[i][j - 1] + self.diff(seq_2[j - 1], '-')

    def alignment(self, i, j, seq_1, seq_2):
        return self.D[i - 1][j - 1] + self.diff(seq_1[i - 1], seq_2[j - 1])

    """Calculates the edit distance and backtrace matrix for two strings
    
    Returns:
        int, [list[list]] -- edit distance, 2D array of values used for backtrace
    """
    def align(self, seq_1, seq_2):
        self.D = [[ 0 for j in range(len(seq_2) + 1)] for i in range(len(seq_1) + 1)]
        ptr = [[ 0 for j in range(len(seq_2) + 1)] for i in range(len(seq_1) + 1)]
        # 0 = DELETION
        # 1 = INSERTION
        # 2 = ALIGN
        self.D[0][0] = 0
        for i in range(1, len(seq_1) + 1):
            self.D[i][0] = self.D[i - 1][0] + self.diff(seq_1[i - 1], '-')
        for j in range(1, len(seq_2) + 1):
            self.D[0][j] = self.D[0][j - 1] + self.diff(seq_2[j - 1], '-')

        for i in range(1, len(seq_1) + 1):
            for j in range(1, len(seq_2) + 1):
                self.D[i][j] = min(
                                self.deletion(i, j, seq_1, seq_2),
                                self.insertion(i, j, seq_1, seq_2),
                                self.alignment(i, j, seq_1, seq_2)
                )
                if (self.D[i][j] == self.deletion(i, j, seq_1, seq_2)):
                    ptr[i][j] = 0
                elif (self.D[i][j] == self.insertion(i, j, seq_1, seq_2)):
                    ptr[i][j] = 1
                else:
                    ptr[i][j] = 2
        return self.D[len(seq_1)][len(seq_2)], ptr
