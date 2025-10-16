from typing import List
from collections import defaultdict

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        buckets = defaultdict(list)
        for point in points:
            buckets[point[0]].append(point[1])
        cnt = 0
        idxs = sorted(list(buckets.keys()))
        print(buckets)
        print(idxs)
        for i in range(1, len(idxs)):
            ii = idxs[i]
            print("ii", ii)
            buckets[ii].sort()
            for jj in buckets[ii]:
                flg = True
                ci = i
                while flg and ci >= 0:
                    for kk in buckets[idxs[ci-1]]:
                        print(i, jj, kk, cnt)
                        if kk >= jj:
                            cnt += 1
                            flg = False
                            break
                    ci -= 1
        for b in buckets.values():
            cnt += len(b)-1
        print("cnt", cnt)
        return cnt 

    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if i == j:continue
                down, right = points[i]
                up, left = points[j]
                print(i, j, up, down, left, right)
                if up >= down and right >= left:
                    print("enter")
                    flg = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        print("?", x, y)
                        if (down <= x <= up and left <= y <= right):
                            print("false?")
                            flg = False
                            break
                    if flg:
                        print("vld", i, j)
                        cnt += 1
        print(cnt)
        return cnt
    
su = Solution()
# case bug
points = [[0,1],[1,3],[6,1]]
ans = 2
res = su.numberOfPairs(points)
assert(res == ans)

# case std1
points = [[6,2],[4,4],[2,6]]
ans = 2
res = su.numberOfPairs(points)
assert(res == ans)





