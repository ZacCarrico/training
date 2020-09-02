"""
sort of like a board game, given an array you see if the values can get you to the end of the array
for example, [3,3,1,0,2,0,1] would get you to the nd of the array b/c you could hop from index 0 -> 1 -> 4 -> 6 -> end
example of what wouldn't get you to the end is [3,3,1,0,0,2,0,1]
write a function that returns True if you can reach the end or False if you can't
patterns:
* keeping track of hte max seen so far in the array
lessons learned:
* the while clause was the trickiest part, specifically the i <= furthest_space. This clause stops the loop
  if the iteration exceeds how far the piece could go in the board game
"""
import unittest


def can_reach_finish(arr):
    i = 0
    furthest_space = arr[0]
    while i <= furthest_space  and furthest_space <= (len(arr) - 1):
        furthest_space = max(furthest_space, arr[i] + i)
        i += 1
    return furthest_space > (len(arr) - 1)

class TestCanReachFinish(unittest.TestCase):
    def test_can_reach_finish(self):
        assert(can_reach_finish([3,3,1,0,2,0,1]) == True)
        assert(can_reach_finish([3,3,1,0,0,2,0,1]) == False)

if __name__ == "__main__":
    unittest.main()