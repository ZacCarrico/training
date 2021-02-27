# report kmer stats: location and total count
from typing import Tuple

def report_subseq_stats(seq: str, subseq: str) -> Tuple[list, int]:
    locations = []
    count = 0
    k = len(subseq)
    for i in range(0,len(seq) - k + 1):
        if seq[i:i+k] == subseq:
            locations.append(i)
            count += 1
    return (locations, count)

def test_report_subseq_stats():
    assert report_subseq_stats("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT") == ([3, 12, 22], 3)
    assert report_subseq_stats("CGATATATCCATAG", "ATA") == ([2, 4, 10], 3)