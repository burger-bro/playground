from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subsequence: dict[int: set] = {}
        for i in range(n):
            for j in range(i+1, n):
                sums = (nums[i] + nums[j])%k
                if sums not in subsequence:
                    subsequence[sums] = set([i, j])
                else:
                    subsequence[sums].add(i)
                    subsequence[sums].add(j)
        print(subsequence)
        ret = 0
        for k,v in subsequence.items():
            ret = max(ret, len(v))
        print(ret)
        return ret

    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0]*k for _ in range(k)]
        ret = 0
        for num in nums:
            cur_rem = num%k
            for prev_rem in range(k):
                dp[prev_rem][cur_rem] = dp[cur_rem][prev_rem] + 1
                ret = max(ret, dp[prev_rem][cur_rem])
        return ret

su = Solution()
# case std1
nums = [1,2,3,4,5]
k = 2
res = su.maximumLength(nums, k)
ans = 5
assert(res == ans) 

# case std2
nums = [1,4,2,3,1,4]
k = 3
res = su.maximumLength(nums, k)
ans = 4
assert(res == ans) 
