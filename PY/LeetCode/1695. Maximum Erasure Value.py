from typing import List 
from collections import deque

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen_set = set()
        seen_seq = deque([])
        sums = 0
        ret = 0
        for n in nums:
            while n in seen_set:
                seen_set.discard(seen_seq[0])
                sums -= seen_seq[0]
                seen_seq.popleft()
            seen_set.add(n)
            seen_seq.append(n)
            sums += n
            # ret = max(ret, sums)
            if sums > ret:
                print(sums, seen_seq)
                ret = sums
        print(ret)
        return ret
    
    def help(self):
        nums = [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
        length = len(nums)
        from collections import Counter
        d = Counter(nums)
        print(d)
        for i in range(length):
            sums = 0
            for j in range(i, length):
                sums += nums[j]
                if sums == 16911:
                    print("debug", i, j)
                    print(nums[i:j+1])

su = Solution()
# case bug
nums = [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
res = su.maximumUniqueSubarray(nums)
ans = 16911
assert(res == ans)

# case std1
nums = [4,2,4,5,6]
res = su.maximumUniqueSubarray(nums)
ans = 17
assert(res == ans)

