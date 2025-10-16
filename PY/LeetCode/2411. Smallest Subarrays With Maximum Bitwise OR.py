from typing import List
from collections import defaultdict

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """
        we need to know for every starting i, how much is its
        max or, and if there exists multiple max, record the shortest one
        but the method cost O(n^2)
        can we trace the max_or during the iterate of i?
        if so, we can half the time to calculate max_or, 
        but we still need to find the length of max_or,
        that have the worst cost of O(n^2)
        """
        or_bit = defaultdict(int)
        for n in nums:
            bit_v = bin(n)[2:]
            for i, b in enumerate(bit_v):
                or_bit[(len(bit_v)-1-i)] += 1 if b=='1' else 0
        print(or_bit)

        ret = []
        for i in range(len(nums)):
            max_or = ''
            for b in range(len(or_bit)):
                max_or = ('1' if or_bit[b] else '0') + max_or
            max_or = int(max_or, base=2)
            # print("max_or", max_or)
            cur_or = 0
            for j in range(i, len(nums)):
                cur_or |= nums[j]
                if cur_or == max_or:
                    ret.append(j-i+1)
                    break
            # update or_bit
            bit_v = bin(nums[i])[2:]
            for i, b in enumerate(bit_v):
                or_bit[(len(bit_v)-1-i)] -= 1 if b=='1' else 0

        print(ret)
        return ret

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        pos = [-1] * 32
        ret = [-1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            j = i
            for p in range(len(pos)):
                if nums[i] & (1<<p) == 0:
                    if pos[p] != -1:
                        j = max(j, pos[p])
                else:
                    pos[p] = i
            ret[i] = j-i+1
        return ret

su = Solution()
# case std1
nums = [1,0,2,1,3]
ans = [3,3,2,2,1]
res = su.smallestSubarrays(nums)
assert(res == ans)

# case std1
nums = [1,2]
ans = [2,1]
res = su.smallestSubarrays(nums)
assert(res == ans)


