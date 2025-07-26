from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        seen = -1
        for n in nums:
            if seen == -1:
                seen = n
                continue
            if n - seen > k:
                cnt += 1
                seen = n

        return cnt+1


