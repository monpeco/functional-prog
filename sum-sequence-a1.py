def sum(seq):
    if len(seq) == 0: return 0
    return seq[0] + sum(seq[1:])

