from collections import Counter
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        d = Counter(s)
        valid_chars = [c for c, v in d.items() if v >= k]
        valid_chars.sort()

su = Solution()
# case std1
s = "letsleetcode"
k = 2
res = su.longestSubsequenceRepeatedK(s, k)
ans = "let"
assert(res == ans)
