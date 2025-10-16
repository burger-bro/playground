from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ud = []
        for i in range(m):
            flag = False
            for j in range(n):
                if grid[i][j] == 1:
                    flag = True
                    break
            ud.append(flag)
        lr = []
        for j in range(n):
            flag = False
            for i in range(m):
                if grid[i][j] == 1:
                    flag = True
                    break
            lr.append(flag)
        l = 0
        for i in range(n):
            if lr[i]:
                l = i
                break
        r = 0
        for i in range(n-1, -1, -1):
            if lr[i]:
                r = i
                break
        u = 0
        for i in range(m):
            if ud[i]:
                u = i
                break
        d = 0
        for i in range(m-1, -1, -1):
            if ud[i]:
                d = i
                break
        print(r,l,u,d)
        return (r-l+1)*(d-u+1)

    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        l, r, u, d = -1, -1, -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    u = i
                    break
            if u != -1: break
        for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j] == 1:
                    d = i
                    break
            if d != -1:break
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    l = j
                    break
            if l != -1: break
        for j in range(n-1, -1, -1):
            for i in range(m):
                if grid[i][j] == 1:
                    r = j
                    break
            if r != -1: break
        print(r,l,u,d)
        return (r-l+1)*(d-u+1)

su = Solution()
# case std1
grid = [[0,1,0],[1,0,1]]
res = su.minimumArea(grid)
ans = 6
assert res == ans, f"Expected {ans}, but got {res}"


