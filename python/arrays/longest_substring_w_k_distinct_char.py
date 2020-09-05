"""
Find the longest substring with k distinct characters
patterns:
* sliding window
lessons learned:
* you need to subtract 1 from end - start
"""
import unittest


def get_length_of_longest_substring_w_k_distinct_char(s: str, k: int) -> int:
    longest_substring_seen_so_far = 0
    for start in range(len(s)):
        end = start + 1
        unique_character_count = 0
        while unique_character_count <= k and end <= len(s):
            longest_substring_seen_so_far = max(longest_substring_seen_so_far, end - start - 1)
            unique_character_count = len(set(s[start:end]))
            end += 1
    return longest_substring_seen_so_far

class TestGetLengthOfLongestSubstringWithKDistinctChar(unittest.TestCase):
    def test(self):
        print(get_length_of_longest_substring_w_k_distinct_char('abccccddef', 2))
        assert(get_length_of_longest_substring_w_k_distinct_char('abccccddef', 2) == 6)

if __name__ == "__main__":
    unittest.main()