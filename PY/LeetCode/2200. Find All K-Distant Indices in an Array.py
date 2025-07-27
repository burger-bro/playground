from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = [i for i, num in enumerate(nums) if num == key]
        ret = []
        for i in range(len(nums)):
            for j in key_indices:
                if abs(i - j) <= k:
                    ret.append(i)
                    break
        return ret