class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            max_diff = max(max_diff, abs(prev-nums[i]))
            prev = nums[i]
        max_diff = max(max_diff, abs(nums[0]-nums[-1]))
        return max_diff
