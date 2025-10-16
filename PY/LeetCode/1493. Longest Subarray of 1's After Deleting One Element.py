from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.reverse()
        delete = False
        cur = 0
        ret = 0
        start = 0
        while start < len(nums) and nums[start] == 0:
            start += 1
        for i in range(start, len(nums)):
            if nums[i] == 1:
                cur += 1
            elif nums[i] == 0:
                if delete:
                    ret = max(cur, ret)
                    cur = 0
                    delete = False
                else:
                    delete = True
                    pass
            print(i, cur)
        ret = max(ret, cur - (0 if delete else 1))
        print(ret)
        return ret

    def longestSubarray(self, nums: List[int]) -> int:
        def helper(nums):
            delete = False
            cur = 0
            ret = 0
            start = 0
            last_start = 0
            while start < len(nums) and nums[start] == 0:
                start += 1
            i = start
            while i < len(nums):
                if nums[i] == 1:
                    cur += 1
                elif nums[i] == 0:
                    if delete:
                        ret = max(cur, ret)
                        cur = 0
                        delete = False
                        i = last_start
                    else:
                        last_start = i
                        delete = True
                print(i, cur)
                i += 1
            ret = max(ret, cur - (0 if delete else 1))
            print(ret)
            return ret
        return max(helper(nums), helper(nums[::-1]))



su = Solution()
# case bug
nums = [1,0,0,0,0]
res = su.longestSubarray(nums)
ans = 1
assert(res == ans)
# case std1
nums = [1,1,0,1]
res = su.longestSubarray(nums)
ans = 3
assert(res == ans)
# case std2
nums = [0,1,1,1,0,1,1,0,1]
res = su.longestSubarray(nums)
ans = 5
assert(res == ans)
# case std3
nums = [1,1,1]
res = su.longestSubarray(nums)
ans = 2
assert(res == ans)
