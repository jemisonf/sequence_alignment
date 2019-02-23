import random
import string


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
        """Get the cost of substituting character x with character y

        Args:
            x (str): Character x
            y (str): Character y

        Returns:
            int: The cost of substitution
        """

        if x in self.cost_dict and y in self.cost_dict[x]:
            return self.cost_dict[x][y]
        else:
            exit(f'Error: could not find cost for ({x}, {y})')

    def get_pairs(self, filename='imp2input.txt'):
        """Get the pairs of strings given in the input file

        Args:
            filename (str, optional): Defaults to 'imp2input.txt'. The name of
                the input file

        Returns:
            List[Tuple[str, str]]: The list of all pairs of strings
        """

        with open(filename) as f:
            pairs = list(map(
                lambda it: tuple(it.strip('\n').split(',')),
                f.readlines()
            ))
        return pairs

    def write_output(self, outputs, filename='imp2output.txt'):
        """Writes the list of outputs to the output file

        Args:
            outputs (List[Tuple[str, str, int]]): A list of tuples where each
                item is the first string, the second string, and the computed
                edit distance, respectively
            filename (str, optional): Defaults to 'imp2output.txt'. The output
                filename
        """

        with open(filename, 'w') as f:
            lines = list(map(
                lambda it: f'{it[0]},{it[1]}:{it[2]}\n',
                outputs
            ))
            f.writelines(lines)

    def reconstruct_ptr(self, pair, ptr):
        """Reconstruct a pair of strings using a backtrace

        Args:
            pair (Tuple[str, str]): A pair of strings. The first string should
                correspond to the x-axis in ptr and the second string should
                correspond to the y-axis
            ptr (List[List[int]]): A backtrace 2-D list where each item
                represents a DELETION, INSERTION, or ALIGNMENT

        Returns:
            Tuple[str, str]: The reconstructed strings, in the same order as
                the strings given in pair
        """

        DELETION = 0
        INSERTION = 1
        ALIGNMENT = 2

        str1 = pair[0]
        str2 = pair[1]
        i = len(str1)
        j = len(str2)
        while not (i <= 0 or j <= 0):
            if ptr[i][j] == DELETION:
                str2 = str2[:j] + '-' + str2[j:]
                i = i - 1
            elif ptr[i][j] == INSERTION:
                str1 = str1[:i] + '-' + str1[i:]
                j = j - 1
            elif ptr[i][j] == ALIGNMENT:
                i = i - 1
                j = j - 1
            else:
                exit(f'Error: invalid value {ptr[i][j]} found in ptr')

        while len(str1) < len(str2):
            str1 = '-' + str1
        while len(str2) < len(str1):
            str2 = '-' + str2

        return (str1, str2)
    
    def make_pair(self, str_length):
        str1 = "".join(random.choice("AGTC") for _ in range(str_length))
        str2 = "".join(random.choice("AGTC") for _ in range(str_length))
        return [str1, str2]

    def write_input(self, pairs, filename="imp2input.txt"):
        with open(filename, 'w') as f:
            lines = list(map(
                lambda it: f'{it[0]},{it[1]}\n',
                pairs
            ))
            f.writelines(lines)


