from typing import List
import math

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        p = 2**30
        powers = []
        while n:
            if p > n:
                p = p >> 1
                continue
            powers.append(int(math.log2(p)))
            n -= p
        powers.sort()
        print(powers)
        prefix_sum = [0] + powers
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
        print(prefix_sum)
        ret = []
        for l, r in queries:
            ai = pow(2, (prefix_sum[r+1]-prefix_sum[l]), mod=MOD)
            ret.append(ai)
        print(ret)
        return ret




su = Solution()
# case std1
n = 15
queries = [[0,1],[2,2],[0,3]]
res = su.productQueries(n, queries)
ans = [2,4,64]
assert(res == ans)        

# case std2
n = 2
queries = [[0,0]]
res = su.productQueries(n, queries)
ans = [2]
assert(res == ans)
