from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # bottom-left
        n = len(grid)
        cur = [0, 0]
        while 0 <= cur[0] < n and 0 <= cur[1] < n:
            integers = []
            cc = cur.copy()
            while 0 <= cc[0] < n and 0 <= cc[1] < n:
                integers.append(grid[cc[0]][cc[1]])
                cc[0] += 1
                cc[1] += 1
            integers.sort()
            cc = cur.copy()
            while 0 <= cc[0] < n and 0 <= cc[1] < n:
                grid[cc[0]][cc[1]] = integers.pop()
                cc[0] += 1
                cc[1] += 1
            cur[0] += 1
        
        cur = [0, 1]
        while 0 <= cur[0] < n and 0 <= cur[1] < n:
            integers = []
            cc = cur.copy()
            while 0 <= cc[0] < n and 0 <= cc[1] < n:
                integers.append(grid[cc[0]][cc[1]])
                cc[0] += 1
                cc[1] += 1
            integers.sort(reverse=True)
            cc = cur.copy()
            while 0 <= cc[0] < n and 0 <= cc[1] < n:
                grid[cc[0]][cc[1]] = integers.pop()
                cc[0] += 1
                cc[1] += 1
            cur[1] += 1
        print(grid)
        return grid
            
            




su = Solution()
# case std1
grid = [[1,7,3],[9,8,2],[4,5,6]]
ans = [[8,2,3],[9,6,7],[4,5,1]]
res = su.sortMatrix(grid)
assert(res == ans)
# case std2
grid = [[0,1],[1,2]]
ans = [[2,1],[1,0]]
res = su.sortMatrix(grid)
assert(res == ans)
# case std3
grid = [[1]]
ans = [[1]]
res = su.sortMatrix(grid)
assert(res == ans)
