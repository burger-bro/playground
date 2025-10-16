from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def valid(a, b, c):
            if a + b <= c or \
                a + c <= b or \
                b + c <= a:
                return False
            return True
        n = len(nums)
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if valid(nums[i], nums[j], nums[k]):
                        ret = max(ret, nums[i]+nums[j]+nums[k])
        return ret

    def largestPerimeter(self, nums: List[int]) -> int:
        def valid(a, b, c):
            if a + b <= c or \
                a + c <= b or \
                b + c <= a:
                return False
            return True
        nums.sort(reverse=True)
        n = len(nums)
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if valid(nums[i], nums[j], nums[k]):
                        return nums[i]+nums[j]+nums[k]
        return 0
    
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i + 1] + nums[i + 2] > nums[i]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0