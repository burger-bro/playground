from typing import List 

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_idx = []
        for i, n in enumerate(nums):
            if n == max_num:
                max_idx.append(i)
        
        visited_idx = set()
        ret = 0
        # print(max_idx)
        for idx in max_idx:
            if idx in visited_idx:
                continue
            left, right = idx, idx
            while left>=0 and nums[idx]&nums[left]==nums[idx]:
                left -= 1
                visited_idx.add(left)
            left += 1
            while right<len(nums) and nums[idx]&nums[right]==nums[idx]:
                right += 1
                visited_idx.add(right)
            right -= 1
            # print(right, left)
            ret = max(ret, right-left+1)
        print(ret)
        return ret

    def longestSubarray(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        max_num = max(nums)
        for i in range(len(nums)):
            if nums[i]&nums[i-1] == max_num:
                dp[i] = dp[i-1] + 1 if i > 0 else 1
        print(max_num, dp)
        return max(dp)

su = Solution()
# case std1
nums = [1,2,3,3,2,2]
res = 2
ans = su.longestSubarray(nums)
assert(res == ans)

# case std2
nums = [1,2,3,4]
res = 1
ans = su.longestSubarray(nums)
assert(res == ans)
