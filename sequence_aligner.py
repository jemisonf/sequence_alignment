from align import Aligner


if __name__ == "__main__":
    aligner = Aligner() 
    pairs = aligner.utils.get_pairs()
    outputs = []
    for pair in pairs:
        n, D = aligner.align(pair[0], pair[1])
        alignments = aligner.utils.reconstruct_ptr(pair, D)
        outputs.append([ alignments[0], alignments[1] , n])
    aligner.utils.write_output(outputs)

