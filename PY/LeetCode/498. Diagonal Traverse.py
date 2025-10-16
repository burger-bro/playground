from typing import List 

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        stacks = [[] for _ in range(m+n-1)]
        for i in range(m):
            for j in range(n):
                stacks[i+j].append(mat[i][j])
        ret = []
        for idx, s in enumerate(stacks):
            if idx%2 == 0:
                ret.extend(s[::-1])
            else:
                ret.extend(s)
        print(ret)
        return ret


su = Solution()
# case std1
mat = [[1,2,3],[4,5,6],[7,8,9]]
res = su.findDiagonalOrder(mat)
ans = [1,2,4,7,5,3,6,8,9]
assert(res == ans)

# case std2
mat = [[1,2],[3,4]]
res = su.findDiagonalOrder(mat)
ans = [1,2,3,4]
assert(res == ans)

