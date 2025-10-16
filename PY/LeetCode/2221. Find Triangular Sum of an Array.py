from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        cnt = len(nums)
        while cnt > 1:
            for i in range(cnt):
                nums[i] = (nums[i] + nums[i+1])%10
            cnt -= 1
        return nums[0]

        