# create a dictionary of all subsequences of length k and their count within a seq
# for example f(ACTGACTCCCACCCC, 3) -> {'ACT', 2, 'CTG'
from collections import defaultdict

def get_subseq_counts(seq: str, k: int) -> dict:
    counts = defaultdict(int)
    for i in range(0, len(seq) - k + 1):
        counts[seq[i:i+k]] += 1
    return counts

def test_get_subseq_counts():
    assert get_subseq_counts("ACTGACTCCCACCCC", 3) == \
           {
               'ACT': 2,
               'CTG': 1,
               'TGA': 1,
               'GAC': 1,
               'CTC': 1,
               'TCC': 1,
               'CCC': 3,
               'CCA': 1,
               'CAC': 1,
               'ACC': 1
           }