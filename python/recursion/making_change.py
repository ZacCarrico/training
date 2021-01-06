"""
a function to determine the fewest number
of US currency coins required to reach a target sum

patterns:
* recursion rather than iteration
* nested helper function using the parent's mutable object
 (a list in this case) to append values
* going through the list of possible coins by passing
 A[1:] into the recursive function rather using a for loop

lessons learned:
* remember that for in-place operations like .sort(),
 don't reassign (eg. don't x = x.sort())
* you can't use an immutable value like an int counter
 to sum the counts across iterations. You can only use
 a list or dictionary
"""
from typing import List


def determine_fewest_coins(coin_values: List[int], target: int) -> int:
    coin_values.sort(reverse=True)
    def helper(coin_values, target):
        if len(coin_values) == 1:
            return [1]
        largest_coin_value = coin_values[0]
        coins = target/largest_coin_value
        remaining = target - largest_coin_value * coins
        total_coins.append(determine_fewest_coins(coin_values[1:], remaining))
        return total_coins
    total_coins = []
    return sum(helper(coin_values, target))

def test_determine_fewest_coins():
    coin_values = [1, 5, 10, 25]
    determine_fewest_coins(coin_values, 1) == 1
    determine_fewest_coins(coin_values, 7) == 3
    determine_fewest_coins(coin_values, 101) == 5
    determine_fewest_coins(coin_values, 116) == 7