from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_with_idx = [(num, i) for i, num in enumerate(nums)]
        nums_with_idx.sort()
        nums_min_max = {}
        for num, idx in nums_with_idx:
            if num not in nums_min_max:
                nums_min_max[num] = [idx, idx] # min, max
            else:
                nums_min_max[num][0] = min(idx, nums_min_max[num][0])
                nums_min_max[num][1] = max(idx, nums_min_max[num][1])

        ret = 0
        for k, v in nums_min_max.items():
            if k + 1 in nums_min_max:
                ret = max(ret, nums_min_max[k + 1][1] - v[0] + 1)
        print(nums_min_max)
        print(ret)
        return ret

    def findLHS(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            c_max, c_min = nums[i], nums[i]
            for j in range(i + 1, len(nums)):
                c_max = max(c_max, nums[j])
                c_min = min(c_min, nums[j])
                if c_max - c_min > 1:
                    break
                ret = max(ret, j - i + 1 if c_max - c_min == 1 else 0)
        print(ret)
        return ret

    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        ret = 0
        for k in count:
            if k + 1 in count:
                ret = max(ret, count[k] + count[k + 1])
        print(ret)
        return ret

su = Solution()
# case std1
nums = [1,3,2,2,5,2,3,7]
res = su.findLHS(nums)
ans = 5
assert(res == ans)
