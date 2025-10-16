from typing import List
from collections import deque

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        dq = deque(values)
        ret = float("inf")
        def find(qq, cur_weight):
            nonlocal ret
            if len(qq) == 3:
                cur_weight += qq[0]*qq[1]*qq[2]
                ret = min(ret, cur_weight)                
                return
            # qq[0]作为顶点删除
            w0 = qq[-1]*qq[0]*qq[1]
            qq0 = dq.popleft()
            print("pop", qq0, cur_weight+w0)
            find(qq, cur_weight+w0)
            qq.appendleft(qq0)
            # qq[0]作为边界点，删除qq[-1]
            w1 = qq[-2]*qq[-1]*qq[0]
            print("pop", qq[-1], cur_weight+w1)
            qq1 = qq.pop()
            find(qq, cur_weight+w1)
            qq.append(qq1)
            # 删除qq[1]
            w2 = qq[0]*qq[1]*qq[2]
            print("pop", qq[1], cur_weight+w2)
            qq2 = qq[1]
            qq.remove(qq2)
            find(qq, cur_weight+w2)
            qq.insert(1, qq2)
        find(dq, 0)
        return ret

class Solution:
    def __init__(self):
        self.dp = [[0] * 50 for _ in range(50)]
        
    def minScoreTriangulation(self, values, i=0, j=0, res=0):
        if j == 0:
            j = len(values) - 1
        if self.dp[i][j] != 0:
            return self.dp[i][j]
        for k in range(i + 1, j):
            res = min(res if res != 0 else float('inf'),
                self.minScoreTriangulation(values, i, k) +
                values[i] * values[k] * values[j] +
                self.minScoreTriangulation(values, k, j))
        self.dp[i][j] = res
        return self.dp[i][j]

