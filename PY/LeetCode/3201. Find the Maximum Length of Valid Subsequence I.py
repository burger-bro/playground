from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd, even, flap1, flap2 = 0, 0, 0, 0
        for n in nums:
            if n%2==0:
                even += 1
            else:
                odd += 1
        
        is_even = 0
        is_odd = 1
        for n in nums:
            if n%2==is_even:
                flap1 += 1
                is_even = 1 if is_even == 0 else 0
            if n%2==is_odd:
                flap2 += 1
                is_odd = 1 if is_odd == 0 else 0
        print(even, odd, flap1, flap2)
        return max([even, odd, flap1, flap2])




