"""
If someone can climb stairs 1, 2, or 3 steps at a time,
what are the number of permutations for climbing a
staircase of height n?
lessons learned:
* You can't use a counter. Just return the sum of the functions
* You need to use n <= 1 as one of the base cases
 rather than just n == 1
"""
def step_perms(n):
    cache = {2:2}
    def helper(n):
        if n <= 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = helper(n-1) + helper(n-2) + helper(n-3)
        return cache[n]
    return helper(n)

def test_step_perms():
    assert(step_perms(3) == 4)