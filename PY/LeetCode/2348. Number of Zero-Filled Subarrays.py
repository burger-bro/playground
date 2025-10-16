from typing import List
from collections import defaultdict

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ret = 0
        cnt_zero = 0
        nums.append(-1)
        for n in nums:
            if n == 0:
                cnt_zero += 1
            else:
                ret += sum(i+1 for i in range(cnt_zero))
                cnt_zero = 0
        return ret

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ret = 0
        cnt_zero = 0
        nums.append(-1)
        zeros = defaultdict(int)
        max_zero = 0
        for n in nums:
            if n == 0:
                cnt_zero += 1
            else:
                zeros[cnt_zero] += 1
                max_zero = max(max_zero, cnt_zero)
                cnt_zero = 0
        cur = 0
        for i in range(max_zero):
            cur += i+1
            ret += zeros[i] * cur

        return ret