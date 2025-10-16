from typing import List
from collections import defaultdict

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod_num = []
        for n in nums:
            mod_num.append(n%value)
        mod_num = list(set(mod_num))
        mod_num.sort()
        print(mod_num)
        for i in range(len(mod_num)):
            if i != mod_num[i]:
                return i
        return i+1
    
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod_dict = defaultdict(int)
        for n in nums:
            mod_dict[n%value] += 1
        print(mod_dict)
        if len(mod_dict) < value:
            for i in range(value):
                if i not in mod_dict:
                    return i
        else:
            min_key, min_val = 0, float("inf")
            for k, v in mod_dict.items():
                if v < min_val:
                    min_key = k
                    min_val = v
                elif v == min_val and k<min_key:
                    min_key = k
            print("mink", min_key)
            return min_key + value * min_val

su = Solution()
# case bug
nums = [3,0,3,2,4,2,1,1,0,4]
value = 5
ans = 10
res = su.findSmallestInteger(nums, value)
assert res == ans, f"expect {ans}, but got {res}"

# case std1
nums = [1,-10,7,13,6,8]
value = 5
ans = 4
res = su.findSmallestInteger(nums, value)
assert res == ans, f"expect {ans}, but got {res}"








