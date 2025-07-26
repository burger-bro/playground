from typing import List
from collections import Counter
import math
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n == 1 or n==0: return False
            for i in range(2, int(math.sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        d = Counter(nums)
        for v in d.values():
            if is_prime(v):
                return True
        return False