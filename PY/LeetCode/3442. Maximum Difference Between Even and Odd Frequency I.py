from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        max_odd, min_even = -float("inf"), float("inf")
        for v in c.values():
            if v % 2 == 0:
                min_even = min(min_even, v)
            else:
                max_odd = max(max_odd, v)
        return max_odd - min_even

su = Solution()
# case std1
s = "aaaaabbc"
res = su.maxDifference(s)
ans = 3
assert(res == ans)
# case std2
s = "abcabcab"
res = su.maxDifference(s)
ans = 1
assert(res == ans)
