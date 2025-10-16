from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        f2p = [[False]*n for _ in range(m)]
        f2a = [[False]*n for _ in range(m)]
        for i in range(n):
            f2p[0][i] = True
            f2a[-1][i] = True
        for i in range(m):
            f2p[i][0] = True
            f2a[i][-1] = True
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def flow(r, c, arr, visited):
            # print(r, c)
            if arr[r][c]:
                return True
            for rr, cc in dirs:
                nr, nc = r+rr, c+cc
                if 0 <= nr < m and 0 <= nc < n \
                    and heights[nr][nc] <= heights[r][c] \
                    and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if flow(nr, nc, arr, visited):
                        arr[r][c] = True
                        return True
        # visited = [[False]*n for _ in range(m)]
        # flow(0, 0, f2a, visited)
        print(f2a)
        for i in range(m):
            for j in range(n):
                visited = [[False]*n for _ in range(m)]
                flow(i, j, f2p, visited)
                visited = [[False]*n for _ in range(m)]
                flow(i, j, f2a, visited)
        ret = []
        for i in range(m):
            for j in range(n):
                if f2a[i][j] and f2p[i][j]:
                    ret.append([i, j])
        print(f2a)
        print(f2p)
        return ret
                
su = Solution()
# case bug
heights = [[10,10,10],[10,1,10],[10,10,10]]
ans = [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
res = su.pacificAtlantic(heights)
assert(res == ans)

# case std1
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
ans = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
res = su.pacificAtlantic(heights)
assert(res == ans)
