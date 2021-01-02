"""
sum a string of integers. The string of integers is duplicated k times
"""

def sum_list_of_int(l):
    total = 0
    for i in l:
        total += i
    return total

def sum_string(n, k):
    return int(str(sum_list_of_int([int(i) for i in list(n)])*k))

def test_sum_string():
    assert sum_string("123", 1) == 6
    assert sum_string("123", 2) == 12