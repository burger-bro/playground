from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        def count(i, j, x):
            for ii in range(i, i+x):
                for jj in range(j, j+x):
                    if matrix[ii][jj] == 0:
                        return False
            return True
        
        ret = 0
        for i in range(n):
            for j in range(m):
                max_range = min(n-i, m-j) + 1
                for x in range(1, max_range):
                    if count(i, j, x):
                        ret += 1
                    else:
                        break
        return ret
    
su = Solution()
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
res = su.countSquares(matrix)
ans = 15
assert res == ans, f"Expected {ans}, but got {res}"


