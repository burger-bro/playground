from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        bin_str = []
        longest = 0
        for n in nums:
            bs = bin(n)[2:]
            longest = max(longest, len(bs))
            bin_str.append(bs)
        for i in range(len(bin_str)):
            bin_str[i] = '0'*(longest-len(bin_str[i])) + bin_str[i]
        max_or = 3

        print(bin_str, longest)
        pass

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n
        print(max_or)
        ret = 0
        def dfs(idx, or_value):
            nonlocal ret
            # print(idx, or_value)
            if or_value == max_or:
                ret += 1
            for j in range(idx+1, len(nums)):
                dfs(j, or_value|nums[j])

        dfs(-1, 0)        
        print("ret", ret)
        return ret



su = Solution()
# case std1
nums = [3,1]  # 11 01
res = su.countMaxOrSubsets(nums)
ans = 2
assert(res == ans)

# case std2
nums = [2,2,2]  # 11 
res = su.countMaxOrSubsets(nums)
ans = 7
assert(res == ans)

# case std3
nums = [3,2,1,5]  # 11 
res = su.countMaxOrSubsets(nums)
ans = 6
assert(res == ans)

# case perf
nums = [3,2,1,5,5,13,24252,4,0,5,92,18,23,45,632,64,52,36]  # 11 
res = su.countMaxOrSubsets(nums)
ans = 6
assert(res == ans)
