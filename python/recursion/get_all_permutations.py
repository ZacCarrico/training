"""
function to get all permutations of a string/list

patterns:
* base case is when there's one element left,
 in which case that element is returned
* the first element is moved through all possible positions
 in the result list by using a sliding window-like pattern
 (I picture it more as a sliding window frame):
 yxxx -> xyxx -> xxyx -> xxxy
 The code for this is: perm[:i] + A[0:1] + perm[i:]
"""

def get_all_permutations(elements):
    perms = []
    if len(elements) <= 1:
        return elements
    else:
        for perm in get_all_permutations(elements[1:]):
            for i in range(len(elements)):
                perms.append(perm[:i] + elements[0:1] + perm[i:])
    return perms

def test_get_all_permutations():
    assert get_all_permutations('abc') == ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']