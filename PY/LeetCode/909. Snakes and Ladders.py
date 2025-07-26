from typing import List
from functools import lru_cache
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def idx2coord(idx):
            div, mod = divmod(idx-1, n)
            # print(div, mod)
            row = n-1-div
            col = mod if div%2==0 else n-1-(mod)
            return row, col
        
        glb_min = float("inf")
        def dfs(cur, cnt):
            print(cur, cnt)
            nonlocal glb_min
            if cur == n**2:
                glb_min = cnt
            if cnt >= glb_min or cnt >= n**2:
                return 
            for i in range(min(cur+6,n**2)-cur, 0, -1):
                r, c = idx2coord(cur+i)
                # if cur == 13 and cnt == 2:
                #     print(cur, cnt, i)
                if board[r][c] != -1:
                    dfs(board[r][c], cnt+1)
                else:
                    dfs(cur+i, cnt+1)

        dfs(1, 0)
        print(glb_min)
        return glb_min if glb_min < float("inf") else -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def idx2coord(idx):
            div, mod = divmod(idx-1, n)
            # print(div, mod)
            row = n-1-div
            col = mod if div%2==0 else n-1-(mod)
            return row, col
        
        new_board = [[-1]*n for _ in range(n)]
        for i in range(1, n**2+1):
            r, c = idx2coord(i)
            if board[r][c] != -1:
                nr, nc = idx2coord(board[r][c])
                new_board[nr][nc] = i
        print(new_board)

        @lru_cache(None)
        def dfs(cur):
            print(cur)
            if cur == 1:
                return 0
            cur_min = float("inf")
            for i in range(1, 7):
                if cur-i <= 0: break
                r, c = idx2coord(cur-i)
                if new_board[r][c] != -1:
                    rr = dfs(new_board[r][c])
                else:
                    rr = dfs(cur-i)
                cur_min = min(cur_min, rr)
            return cur_min+1

        ret = dfs(n*n)
        print(ret)
        return ret if ret < float("inf") else -1


    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def idx2coord(idx):
            div, mod = divmod(idx-1, n)
            # print(div, mod)
            row = n-1-div
            col = mod if div%2==0 else n-1-(mod)
            return row, col
        
        queue = deque([[1, 0, set([0])]])

        ret = float("inf")
        while queue:
            cur, cnt, visited = queue.popleft()
            print(cur, cnt)
            if cur == n*n:
                return cnt
            if cnt > n*n:
                return -1
            flag = True
            for i in range(min(cur+6,n**2)-cur, 0, -1):
                r, c = idx2coord(cur+i)
                if cur+i in visited: continue
                new_visited = visited.copy()|{cur+i}
                if board[r][c] != -1:
                    queue.append([board[r][c], cnt+1, new_visited])
                elif flag:
                    flag = False
                    queue.append([cur+i, cnt+1, new_visited])
        print(ret)
        return ret


    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def idx2coord(idx):
            div, mod = divmod(idx-1, n)
            # print(div, mod)
            row = n-1-div
            col = mod if div%2==0 else n-1-(mod)
            return row, col
        
        queue = deque([[1, 0]])

        visited = [[False]*n for _ in range(n)]

        ret = float("inf")
        while queue:
            cur, cnt = queue.popleft()
            print(cur, cnt)
            if cur == n*n:
                return cnt
            if cnt > n*n:
                return -1
            flag = True
            for i in range(min(cur+6,n**2)-cur, 0, -1):
                r, c = idx2coord(cur+i)
                if visited[r][c]: continue
                visited[r][c] = True
                if board[r][c] != -1:
                    queue.append([board[r][c], cnt+1])
                elif flag:
                    flag = False
                    queue.append([cur+i, cnt+1])
        return -1



su = Solution()
#case bug
board = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
res = su.snakesAndLadders(board)

# #case bug
# board = [[1,1,-1],[1,1,1],[-1,1,1]]
# res = su.snakesAndLadders(board)

# #case perf
# board = [[-1,-1,128,-1,-1,-1,136,-1,-1,-1,109,-1],[-1,-1,-1,-1,-1,103,-1,-1,56,10,-1,-1],[-1,-1,-1,-1,-1,-1,116,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,50,-1,67,107],[-1,40,-1,-1,-1,20,-1,59,-1,67,-1,-1],[-1,-1,-1,-1,-1,-1,112,133,111,-1,-1,-1],[-1,-1,112,-1,74,-1,-1,-1,-1,-1,-1,-1],[23,-1,115,-1,129,126,-1,-1,-1,-1,-1,-1],[106,143,81,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,26,102,1,29],[26,-1,-1,-1,-1,-1,-1,-1,27,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
# res = su.snakesAndLadders(board)

# #case std1
# board = [[-1,-1,-1,-1,-1,-1],
#          [-1,-1,-1,-1,-1,-1],
#          [-1,-1,-1,-1,-1,-1],
#          [-1,35,-1,-1,13,-1],
#          [-1,-1,-1,-1,-1,-1],
#          [-1,15,-1,-1,-1,-1]]
# res = su.snakesAndLadders(board)
# ans = 4
# assert(res == ans)

# #case std2
# board = board = [[-1,-1],[-1,3]]
# res = su.snakesAndLadders(board)
# ans = 1
# assert(res == ans)

