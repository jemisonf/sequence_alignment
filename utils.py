

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
