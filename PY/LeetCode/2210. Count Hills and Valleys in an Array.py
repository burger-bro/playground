from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        no_repeat = []
        for n in nums:
            if no_repeat and no_repeat[-1] == n:
                continue
            no_repeat.append(n)
        ret = 0
        for i in range(1, len(no_repeat)-1):
            if no_repeat[i-1] < no_repeat[i] > no_repeat[i+1] or \
            no_repeat[i-1] > no_repeat[i] < no_repeat[i+1]:
                ret += 1
        return ret


su = Solution()

# case std1
nums = [2,4,1,1,6,5]
res = su.countHillValley(nums)
ans = 3
assert(res == ans)

# case std2
nums = [6,6,5,5,4,1]
res = su.countHillValley(nums)
ans = 0
assert(res == ans)
