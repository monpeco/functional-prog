"""
We've defined the sum of a sequence in two cases: the base case states that the
sum of a zero length sequence is 0, while the recursive case states that the sum
of a sequence is the first value plus the sum of the rest of the sequence. Since the
recursive definition depends on a shorter sequence, we can be sure that it will
(eventually) devolve to the base case.
"""
def sum(seq):
    if len(seq) == 0: return 0
    return seq[0] + sum(seq[1:])


s=sum(range(5))
print(s)