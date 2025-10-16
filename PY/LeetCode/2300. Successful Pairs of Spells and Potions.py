from typing import List
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ret = []
        potions.sort()
        n = len(potions)
        for s in spells:
            target = math.ceil(success/s)
            left, right = 0, n
            while left < right:
                mid = left + (right-left)//2
                # if potions[mid] == target:
                #     break
                if potions[mid] < target:
                    left = mid+1
                elif potions[mid] >= target:
                    right = mid
            print(left, right, mid)
            if potions[mid]*s>=success:
                ret.append(n-mid)
            else:
                ret.append(0)
        print(ret)
        return ret




