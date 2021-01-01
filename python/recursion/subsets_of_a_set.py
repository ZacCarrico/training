"""
Generate all subset of a set

lessons learned:
* you need to add the subsets to the first element plus the subsets
* the time complexity of O(n2^n) comes because for each n, it can
 either have or not have that nth index value. You mulitply that by
 n because the recursion goes through each element in the list

patterns:
* recursion

time: O(n*2^n), space: same
"""

def subsets_of_set(A):
    if A == []:
        return [[]]
    subsets = subsets_of_set(A[1:])
    return subsets + [[A[0]] + subset for subset in subsets]

def test_subsets_of_set():
    assert subsets_of_set([1,2,3]) == [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
"""
thinking through the problem
f(123)
    subsets = f(23)
        subsets = f(3) -> [3]
            subsets = f() -> [[]]
        [[]] + [[3] + subset for subset in [[]]] -> [[], [3]]
    [[], [3]] + [[2] + subset for subset in  [[], [3]]] -> [[], [3]] + [[2], [2,3]] -> [[], [3], [2], [2,3]]
[[], [3], [2], [2,3]] + [[1] + subset for subset in [[], [3], [2], [2,3]]] -> [[], [3], [2], [2,3]] + [[1], [1,3], [1,2], [1,2,3]] -> [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
"""