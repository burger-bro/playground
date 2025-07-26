class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        print("begin")
        if n > 3*limit: return 0
        # a_choice = limit - max(n-2*limit, 0) + 1
        # for i in range(1, a_choice+1):
        ret = 0
        for i in range(max(n-2*limit, 0), limit+1):
            ret += max(min(limit, n-i) - max(0, (n-i-limit)) + 1, 0)
            print(i, ret)
        print(ret)
        return ret

su = Solution()
# case bug
n = 1
limit = 3
res = su.distributeCandies(n, limit)
ans = 3
assert(res == ans)

# case std1
n = 5
limit = 2
res = su.distributeCandies(n, limit)
ans = 3
assert(res == ans)

# case std2
n = 3
limit = 3
res = su.distributeCandies(n, limit)
ans = 10
assert(res == ans)
