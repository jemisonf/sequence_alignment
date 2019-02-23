from utils import AlignmentUtils
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        size = sys.argv[1]
        print(size)
        utils = AlignmentUtils()
        pairs = []
        for _ in range(10):
            strings = utils.make_pair(int(size))
            pairs.append(strings)
            print(strings)
        utils.write_input(pairs)



    else:
        print("Please enter one argument for the length of the strings.")
