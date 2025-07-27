from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        """
        what we need to return is the number of subarrays in some special rules.
        1. suppose that there are no restrictions, how do we get the num?
        2. suppose that the restrictions are fixed, how do we get the num?
        3. suppose one conflicpairs can be deleted, ...?

        with this framework, is seems that we can search all possible delete,
        and check if the num is max. but this method might got TLE in 10^5.
        we still didn't work out Q1 and Q2.
        we need a bidirection dict, when we iterate over the array, 
        store the values of seen num in a set, if a new one's key in this
        set, then they are conflict, we could stop here. but this method cost
        O(n^2).
        """
        pass

