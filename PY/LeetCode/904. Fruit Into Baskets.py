from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        l = r = 0
        seen = {}
        ret = 0
        while r < n:
            # print(r, seen)
            if fruits[r] not in seen:
                if len(seen) == 2:
                    while len(seen) == 2:
                        seen[fruits[l]] -= 1
                        if seen[fruits[l]] == 0:
                            del seen[fruits[l]]
                        l += 1
                seen[fruits[r]] = 1
            else:
                seen[fruits[r]] += 1
            ret = max(ret, r-l+1)
            r += 1
            # ret = max(ret, sum(seen.values()))
        return ret

su = Solution()
# case std1
fruits = [1,2,1]
res = su.totalFruit(fruits)
ans = 3
assert(res == ans)
# case std2
fruits = [0,1,2,2]
res = su.totalFruit(fruits)
ans = 3
assert(res == ans)
