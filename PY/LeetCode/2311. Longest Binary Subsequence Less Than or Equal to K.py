class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeros = s.count('0')
        ones = 0
        power = 1
        val = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                if val + power <= k:
                    val += power
                    ones += 1
                else:
                    break
            power *= 2
        return ones + zeros                