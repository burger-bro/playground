from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        fruits.sort(reverse=True)
        m = len(baskets)
        placed = [False] * len(fruits)
        i = 0
        print(fruits)
        while i < m:
            j = 0
            while j < m and (placed[j] or fruits[j]>baskets[i]):
                j += 1
            print(placed)
            if j == m:
                print(m-i)
                return m-i
            placed[j] = True
            i += 1
        print(0)
        return 0
                
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        m = len(fruits)
        i = 0
        placed = [False] * m
        while i < m:
            j = 0
            while j < m and (placed[j] or baskets[j] < fruits[i]):
                j += 1
            i += 1
            if j == m:
                continue
            placed[j] = True
        return placed.count(False)

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        m = len(fruits)
        i = 0
        placed = [False] * m
        while i < m:
            j = 0
            while j < m and (placed[j] or baskets[j] < fruits[i]):
                j += 1
            i += 1
            if j == m:
                continue
            placed[j] = True
        return placed.count(False)

su = Solution()
# case std1
fruits = [4, 2, 5]
baskets = [3, 5, 4]
res = su.numOfUnplacedFruits(fruits, baskets)
ans = 1
assert(res == ans)


        