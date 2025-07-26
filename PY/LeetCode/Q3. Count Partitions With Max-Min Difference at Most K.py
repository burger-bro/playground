from typing import List
from collections import deque
class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        dp[0] = 1
        prefix[0] = 1

        max_deque = deque([])
        min_deque = deque([])
        left = 0
        
        for i in range(1, n + 1):
            num = nums[i - 1]
            while max_deque and nums[max_deque[-1]] <= num:
                max_deque.pop()
            max_deque.append(i - 1)
            while min_deque and nums[min_deque[-1]] >= num:
                min_deque.pop()
            min_deque.append(i - 1)
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            dp[i] = (prefix[i - 1] - (prefix[left - 1] if left > 0 else 0)) % MOD
            prefix[i] = (prefix[i - 1] + dp[i]) % MOD
        
        return dp[n] % MOD


su = Solution()
# case std1
nums = [9,4,1,3,7]
k = 4
res = su.countPartitions(nums, k)
ans = 6
assert(res==ans)
# case std2
nums = [3,3,4]
k = 0
res = su.countPartitions(nums, k)
ans = 2
assert(res==ans)
