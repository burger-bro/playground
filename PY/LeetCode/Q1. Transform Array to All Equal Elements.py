from typing import List

class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        if len(nums)==1: return True
        def helper(nums, target):
            cnt = 0
            idx = 0
            for idx in range(1, len(nums)):
                if nums[idx-1] != target:
                    nums[idx-1] = -nums[idx-1]
                    nums[idx] = -nums[idx]
                    cnt += 1
                if cnt > k:
                    break
            print(nums)
            if cnt <= k and idx == len(nums)-1 and nums[-1] == target:
                return True
            return False
        r1 = helper(nums.copy(), 1)
        r2 = helper(nums.copy(), -1)
        print(r1, r2)
        return r1 or r2
            

su = Solution()
# 1 1 1 1
# - - 1 1
# - 1 - 1
# - - 1 1
#case bug2
nums = [-1]
k = 0
res = su.canMakeEqual(nums, k)
ans = True
assert(res == ans)

#case bug2
nums = [-1]
k = 1
res = su.canMakeEqual(nums, k)
ans = True
assert(res == ans)

#case bug1
nums = [1,-1,1,1,-1,1,1,1,-1]
k = 5
res = su.canMakeEqual(nums, k)
ans = True
assert(res == ans)

#case std1
nums = [1,-1,1,-1,1]
k = 3
res = su.canMakeEqual(nums, k)
ans = True
assert(res == ans)

#case std2
nums = [-1,-1,-1,1,1,1]
k = 5
res = su.canMakeEqual(nums, k)
ans = False
assert(res == ans)
