from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        num_with_idx = []
        for idx, n in enumerate(nums):
            num_with_idx.append([n, idx])
        num_with_idx.sort(key=lambda x: x[0])
        print(num_with_idx)
        
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        print(nums)
        max_diff = 0
        for i in range(0, 2*p, 2):
            print(max_diff)
            max_diff = max(max_diff, abs(nums[i]-nums[i+1]))
        print(max_diff)
        #   1 4 5 9 100
        #   1 2 2 5 100
        return max_diff
    
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n, left, right = len(nums), 0, nums[-1]-nums[0]
        while left < right:
            mid = left + (right-left)//2
            pairs = 0
            i = 0
            while i < n-1:
                if abs(nums[i]-nums[i+1]) <= mid:
                    pairs += 1
                    i += 1
                i += 1
            if pairs >= p:
                right = mid
            else:
                left = mid+1
        return right


su = Solution()
#case std1
nums = [10,1,2,7,1,3]
p = 2
res = su.minimizeMax(nums, p)
ans = 1
assert(res == ans)
#case std2
nums = [4,2,1,2]
p = 1
res = su.minimizeMax(nums, p)
ans = 0
assert(res == ans)

