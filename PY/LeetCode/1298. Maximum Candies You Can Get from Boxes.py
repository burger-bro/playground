from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        remaining_boxes = deque(initialBoxes)
        ret = 0
        key_set = set()
        cnt = 0
        while remaining_boxes:
            cnt += 1
            cur_box = remaining_boxes.popleft()
            if status[cur_box] == 1 or cur_box in key_set:
                ret += candies[cur_box]
                for key in keys[cur_box]:
                    key_set.add(key)
                remaining_boxes.extend(containedBoxes[cur_box])
                cnt = 0
            else:
                remaining_boxes.append(cur_box)
            if cnt == len(remaining_boxes):
                break
        return ret

su = Solution()
# case std1
status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]
res = su.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
ans = 16
assert(res == ans)

# case std2
status = [1,0,0,0,0,0]
candies = [1,1,1,1,1,1]
keys = [[1,2,3,4,5],[],[],[],[],[]]
containedBoxes = [[1,2,3,4,5],[],[],[],[],[]]
initialBoxes = [0]
res = su.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
ans = 6
assert(res == ans)
