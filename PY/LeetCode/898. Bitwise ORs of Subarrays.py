from typing import List 

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ret = set()
        for i in range(len(arr)):
            cur = 0
            for j in range(i, len(arr)):
                cur |= arr[j]
                ret.add(cur)
        return len(ret)

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ret = set()
        tmp = {0}
        for i in range(len(arr)):
            tmp = {x|arr[i] for x in tmp} | {arr[i]}
            ret |= tmp
        return len(ret)

