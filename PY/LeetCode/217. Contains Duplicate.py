from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set:
                return False
            num_set.add(n)
        return True





