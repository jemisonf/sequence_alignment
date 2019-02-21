

class AlignmentUtils:
    def __init__(self, cost_filename='imp2cost.txt'):
        self.cost_dict = self.__parse_cost_dict(cost_filename)

    def __parse_cost_dict(self, filename):
        cost_dict = {}
        with open(filename) as f:
            matrix = list(map(
                lambda it: it.strip('\n').split(','),
                f.readlines()
            ))
            for i in range(1, len(matrix[0])):
                cost_dict[matrix[i][0]] = {}
                for j in range(1, len(matrix[0])):
                    cost_dict[matrix[i][0]][matrix[j][0]] = int(matrix[i][j])
        return cost_dict

    def get_cost(self, x, y):
        if x in self.cost_dict and y in self.cost_dict[x]:
            return self.cost_dict[x][y]
        else:
            exit(f'Error: could not find cost for ({x}, {y})')

    def get_pairs(self, filename='imp2input.txt'):
        with open(filename) as f:
            pairs = list(map(
                lambda it: tuple(it.strip('\n').split(',')),
                f.readlines()
            ))
        return pairs

    def write_output(self, outputs, filename='imp2output.txt'):
        with open(filename, 'w') as f:
            lines = list(map(
                lambda it: f'{it[0]},{it[1]}:{it[2]}\n',
                outputs
            ))
            f.writelines(lines)

    def reconstruct_ptr(self, pair, ptr):
        DELETION = 0
        INSERTION = 1
        ALIGNMENT = 2

        str1 = pair[0]
        str2 = pair[1]
        i = len(str1) - 1
        j = len(str2) - 1
        while i >= 0 and j >= 0:
            if ptr[i][j] == DELETION:
                str2 = str2[:(j + 1)] + '*' + str2[(j + 1):]
                i = i - 1
            elif ptr[i][j] == INSERTION:
                str1 = str1[:(i + 1)] + '*' + str1[(i + 1):]
                j = j - 1
            elif ptr[i][j] == ALIGNMENT:
                i = i - 1
                j = j - 1
            else:
                exit(f'Error: invalid value {ptr[i][j]} found in ptr')
        return (str1, str2)
