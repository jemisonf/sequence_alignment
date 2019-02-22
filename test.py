from align import Aligner
from utils import AlignmentUtils

aligner = Aligner()
utils = AlignmentUtils()

str1 = "AAATGTGTGTGTTCCCCAACGATGTCTCTAGAAGACGAACATCCC"
str2 = "ACTAGATGGAAACGTGAACCTAACTAACACATATGGATCCGACTGACGTTCTCTGATGTAGCCT"
n, ptr = aligner.align(str2, str1)
print(n)
str1_out, str2_out = utils.reconstruct_ptr([str2, str1], ptr)
print(str1_out)
print(str2_out)

"""
pairs = utils.get_pairs("imp2input2.txt")
outlist = []
for pair in pairs:
    n, ptr = aligner.align(pair[0], pair[1])
    outstr1, outstr2 = utils.reconstruct_ptr(pair, ptr)
    outlist.append([outstr1, outstr2, n])
"""

# utils.write_output(outlist)

