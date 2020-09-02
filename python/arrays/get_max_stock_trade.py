"""
get the maximum stock trade revenue given an array of stock prices for the same stock. Each element is a different day
for example if [3, 2, 10, 8, 12, 1, 0] is the array, the max would be to by at 2 and sell at 12 for a revenue of 10
patterns:
* keep track of min value seen
* keep track of max diff seen
lessons learned:
* the insight is that you're not comparing min of the array to the max of the array, but the min/max of subarrays.
*  these subarrays are simply what you have seen so far

* O(n) time, O(1) space
"""
import unittest

def get_max_stock_trade(arr):
    min_seen = arr[0]
    max_stock_trade = 0
    for val in arr:
        current_diff = val - min_seen
        min_seen = min(min_seen, val)
        max_stock_trade = max(max_stock_trade, current_diff)
    return max_stock_trade

class TestGetMaxStockTrade(unittest.TestCase):
    def test_get_max_stock_trade(self):
        assert(get_max_stock_trade([3, 2, 10, 8, 12, 1, 0]) == 10)

if __name__ == '__main__':
    unittest
