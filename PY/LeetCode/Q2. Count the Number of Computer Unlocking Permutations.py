from typing import List
from functools import lru_cache

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if min(complexity[1:]) <= complexity[0]: return 0
        MOD = 10*9+7
        @lru_cache(None)
        def dfs(idx):
            if idx == len(complexity)-1:
                return 1
            ret = 0
            for i in range(idx+1, len(complexity)):
                # if complexity[i] > complexity[idx]:
                ret += dfs(i)
                ret %= MOD
            print(idx, ret)
            return ret
        
        rr = dfs(0)
        print(rr)
        return rr

    def countPermutations(self, complexity: List[int]) -> int:
        if min(complexity[1:]) <= complexity[0]: return 0
        ret = 1
        MOD = 10**9+7
        for i in range(1, len(complexity)):
            print(i)
            ret *= i
            ret %= MOD
        print(ret)
        return ret

su = Solution()
# case bug
complexity = [103,274,183,473,487,304,407]
res = su.countPermutations(complexity)
ans = 720
assert(res == ans)

# case bug
complexity = [155,437,368,168]
res = su.countPermutations(complexity)
ans = 6
assert(res == ans)


# case bug
complexity = [2,68,61]
res = su.countPermutations(complexity)
ans = 2
assert(res == ans)

# case std1
complexity = [1,2,3]
res = su.countPermutations(complexity)
ans = 2
assert(res == ans)
# case std2
complexity = [3,3,3,4,4,4]
res = su.countPermutations(complexity)
ans = 0
assert(res == ans)