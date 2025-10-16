class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_2 = set()
        x = 1
        while x <= 10**9:
            power_of_2.add(''.join(sorted(str(x))))
            x *= 2
        return ''.join(sorted(str(n))) in power_of_2

su = Solution()
# case std1
n = 1
res = su.reorderedPowerOf2(n)
ans = True
assert(res == ans)

# case std2
n = 10
res = su.reorderedPowerOf2(n)
ans = False
assert(res == ans)
