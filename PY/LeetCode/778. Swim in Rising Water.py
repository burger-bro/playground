from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        heap = [[grid[0][0], 0, 0]]
        heapq.heapify(heap)
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        t = 0
        while heap:
            tt, r, c = heapq.heappop(heap)
            t = max(tt, t)
            if r==m-1 and c==n-1: 
                break
            # print(r,c,t)
            for rr, cc in dirs:
                nr, nc = r+rr, c+cc
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(heap, [grid[nr][nc], nr,nc])
        # print(t)
        return t



su = Solution()
# case std1
grid = [[0,2],[1,3]]
ans = 3 
res = su.swimInWater(grid)
assert(res == ans)

# case std2
grid = grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
ans = 16
res = su.swimInWater(grid)
assert(res == ans)

