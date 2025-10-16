class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        ps = []
        p = 1
        while p**x <= n:
            ps.append(p**x)
            p += 1
        ret = 0
        print(ps)
        def dfs(cur_sum, idx):
            nonlocal ret
            # print(cur_sum, idx)
            if cur_sum > n:
                return 
            if cur_sum == n:
                ret += 1
                return 
            for i in range(idx+1, len(ps)):
                dfs(cur_sum+ps[i], i)
        dfs(0, -1)
        print(ret)
        return ret

    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            val = i**x
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= val:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD
        return dp[n][n]



su = Solution()
# case perf
n = 75
x = 1
res = su.numberOfWays(n, x)
ans = 2


# case std1
n = 10
x = 2
res = su.numberOfWays(n, x)
ans = 1
assert(res == ans)

# case std2
n = 4
x = 1
res = su.numberOfWays(n, x)
ans = 2
assert(res == ans)


