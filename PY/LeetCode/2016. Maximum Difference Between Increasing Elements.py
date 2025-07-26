from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ret = -1
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[j]-nums[i]
                if diff > 0:
                    ret = max(ret, diff)
        return ret
    
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        right_max[-1] = nums[-1]
        ret = -1
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
        for i in range(n-1):
            diff = right_max[i]-nums[i]
            if diff > 0:
                ret = max(diff, ret)
        return ret

        
