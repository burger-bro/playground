from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        nums.append(float("-inf"))
        diff = []
        for i in range(len(nums)-1):
            diff.append(True if nums[i+1]-nums[i]>0 else False)
        ret = 0
        max_cnt = 0
        max_len = []
        connection_flag = False
        print(diff)
        for i in range(len(diff)):
            print(ret, max_cnt, max_len)
            if diff[i]:
                max_cnt += 1
            else:
                if connection_flag:
                    ret = max(min(max_len[-1], max_cnt), ret)
                if i+1<len(diff) and diff[i+1]:
                    connection_flag = True
                max_len.append(max_cnt)
                ret = max(ret, (max_cnt-1)//2)
                max_cnt = 0
        return ret + 1

su = Solution()
# case bug2
nums = [-10,14,17]
ans = 1
res = su.maxIncreasingSubarrays(nums)
assert(res == ans)

# case bug
nums = [5,8,-2,-1]
ans = 2
res = su.maxIncreasingSubarrays(nums)
assert(res == ans)

