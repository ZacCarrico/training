"""
Write a function to get the number of occurrences of a
substring in a string
Example
str: abbcabdabdefbbcabb
substr: abbc
f(str, substr) -> 6

patterns:
* use the ascii ordinal encoding of letters
* create a dictionary-like representation using a
 list by using the index number as the key, and
 that index's element value as the value
 * for this solution, the index is the ordinal
 encoding of a letter (using ascii to set ordinal
 values) and the element's value is a count
* populate counts for list indexes first,
 then iterate
* helper function to compare lists

time complexity: O(n)
space complexity: O(1)
"""


def is_match(a: dict, b: dict) -> bool:
    if a != b:
        return False
    return True

def get_number_occurrences_substr_in_str(s: str, b: str) -> int:
    b_counts = [0]*256
    s_window_counts = [0]*256
    substrs_permutations_in_s = 0

    # prepping the count objects
    for i in range(len(b)):
        b_counts[ord(b[i])] += 1
        s_window_counts[ord(s[i])] += 1

    # compares the count objects, then adds/subtracts
    #  from the index's count starting after the length
    #  of the substr
    for i in range(len(b), len(s)):
        if is_match(b_counts, s_window_counts):
            substrs_permutations_in_s += 1

        s_window_counts[ord(s[i])] += 1
        s_window_counts[ord(s[i-len(b)])] -= 1

    if is_match(b_counts, s_window_counts):
        substrs_permutations_in_s += 1

    return substrs_permutations_in_s

def test_get_number_occurrences_substr_in_str():
    assert(get_number_occurrences_substr_in_str('abbcabdabdefbbcabb', 'abbc') == 6)
