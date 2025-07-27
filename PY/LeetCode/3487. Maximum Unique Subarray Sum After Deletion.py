class Solution:
    def maxSum(self, nums) -> int:
        ret = 0
        seen = set()
        sums = 0
        for n in nums:
            if n in seen or (n<0 and sums !=0):
                seen.clear()
                ret = max(ret, sums)
                sums = 0
            seen.add(n)
            sums += n
        return max(ret, sums)

    def maxSum(self, nums) -> int:
        ret = 0
        seen = set()
        sums = 0
        for n in nums:
            if n in seen:
                continue
            seen.add(n)
            sums += n
        return max(ret, sums)

    def maxSum(self, nums) -> int:
        if max(nums) <= 0: return max(nums)
        sums = 0
        seen = set()
        for n in nums:
            if n in seen or n <= 0:
                continue
            sums += n
            seen.add(n)
        return  sums


su = Solution()
# case std1
nums = [1,2,3,4,5]
res = su.maxSum(nums)
ans = 15
assert(res == ans)

# case std1
nums = [1,1,0,1,1]
res = su.maxSum(nums)
ans = 1
assert(res == ans)

# case std1
nums = [1,2,-1,-2,1,0,-1]
res = su.maxSum(nums)
ans = 3
assert(res == ans)

