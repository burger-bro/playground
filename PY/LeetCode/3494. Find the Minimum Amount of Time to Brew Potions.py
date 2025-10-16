from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        l = len(skill)
        last_time = [0]*l
        for m in mana:
            cur_time = [0]*l
            lt = last_time[0]
            for i in range(l):
                cur_time[i] = lt + m*skill[i]
                lt = cur_time[i]
            offset = 0
            for i in range(l-1):
                if cur_time[i]+offset < last_time[i+1]:
                    offset += last_time[i+1]-(cur_time[i]+offset)
            last_time = [t+offset for t in cur_time]
        return last_time[-1]

su = Solution()
# case std1
# 5 30 40 60
skill = [1,5,2,4]
mana = [5,1,4,2]
ans = 110
res = su.minTime(skill, mana)
assert(res == ans)


            


