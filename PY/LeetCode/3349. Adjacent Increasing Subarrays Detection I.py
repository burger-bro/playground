from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        diff = []
        for i in range(len(nums-1)):
            if nums[i+1]-nums[i] > 0:
                diff.append(True)
            else:
                diff.append(False)
        

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        diff = []
        cnt = 0
        success = 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] > 0:
                cnt += 1
            else:
                if cnt == 0:
                    success = 0
                cnt = 0
            if cnt >= 2*(k-1)+1:
                return True
            if cnt == k-1:
                success += 1
            if success == 2:
                return True
            print(nums[i+1]-nums[i], cnt, success)
        return False
        

su = Solution()
nums = [2,5,7,8,9,2,3,4,3,1]
k = 3
ans = True
res = su.hasIncreasingSubarrays(nums, k)
assert(res == ans)
print("********************")
nums = [-15,-13,4,7]
k = 2
ans = True
res = su.hasIncreasingSubarrays(nums, k)
assert(res == ans)
print("********************")
nums = [463,-724,-568,415,49,977,-858,-523,243,486,149,155,-397,915,-661,458,-248,540]
k = 3
ans = False
res = su.hasIncreasingSubarrays(nums, k)


