from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # b1c = Counter(basket1)
        # b2c = Counter(basket2)
        basket1.sort()
        basket2.sort()
        print(basket1)
        print(basket2)
        i = j = 0
        n = len(basket1)
        b1_r, b2_r = [], []
        while i < n and j < n:
            if basket1[i] == basket2[j]:
                i += 1
                j += 1
                continue

            if i == n-1 or j == n-1:
                return -1

            if basket1[i] < basket2[j]:
                i += 1
                if basket1[i] != basket1[i-1]:
                    return -1
                basket1[i], basket2[j] = basket2[j], basket1[i]
                b1_r.append(basket1[i])
                b2_r.append(basket2[j])
                j += 1
            else:
                j += 1
                if basket2[j] != basket2[j-1]:
                    return -1
                basket1[i], basket2[j] = basket2[j], basket1[i]
                b1_r.append(basket1[i])
                b2_r.append(basket2[j])
                i += 1
            
        print(basket1, basket2)
        print(b1_r, b2_r)
        b1_r.sort(reverse=True)
        b2_r.sort(reverse=True)
        ret = 0
        cnt = len(b1_r)
        while cnt:
            if b1_r[-1] < b2_r[-1]:
                ret += b1_r.pop()
            else:
                ret += b2_r.pop()
            cnt -= 1
        print(ret)
        return ret
            
            



"""
11222345
11222345

11222244
11223355

11222245
11222245

11222222
11224455

"""

su = Solution()
# case bug
basket1 = [84,80,43,8,80,88,43,14,100,88]
basket2 = [32,32,42,68,68,100,42,84,14,8]
res = su.minCost(basket1, basket2)
ans = 48
assert(res == ans)

# case std1
basket1 = [4,2,2,2]
basket2 = [1,4,1,2]
res = su.minCost(basket1, basket2)
ans = 1
assert(res == ans)

# case std2
basket1 = [2,3,4,1]
basket2 = [3,2,5,1]
res = su.minCost(basket1, basket2)
ans = -1
assert(res == ans)
