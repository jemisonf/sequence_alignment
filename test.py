from align import Aligner, print_matrix
from utils import AlignmentUtils

aligner = Aligner()
utils = AlignmentUtils()
print("*,-,A,T,G,C")
for char in "-ATGC":
    print(char, end=",")
    for char2 in "-":
        print(utils.get_cost(char, char2), end=",")
    print("\n", end="")

str1 = "AATC"
str2 = "ATC"
n, ptr = aligner.align(str1, str2)
print(n)
# print_matrix(ptr)
str1_out, str2_out = utils.reconstruct_ptr([str1, str2], ptr)
print(str1_out)
print(str2_out)

pairs = utils.get_pairs("imp2input.txt")
outlist = []
numerrs = 0
for pair in pairs:
    n, ptr = aligner.align(pair[0], pair[1])
    outstr1, outstr2 = utils.reconstruct_ptr(pair, ptr)
    if (len(outstr1) != len(outstr2)):
        numerrs += 1
        print(f"error on {pair}")
        print(f"\t{outstr1}")
        print(f"\t{outstr2}")
        print()
    outlist.append([outstr1, outstr2, n])

print(f"num errs: {numerrs}")

utils.write_output(outlist)
