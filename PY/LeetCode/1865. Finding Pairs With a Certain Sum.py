from typing import List
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts = {}
        for num in nums2:
            if num in self.counts:
                self.counts[num] += 1
            else:
                self.counts[num] = 1

    def add(self, index: int, val: int) -> None:
        self.counts[self.nums2[index]] -= 1
        if self.counts[self.nums2[index]] == 0:
            del self.counts[self.nums2[index]]
        self.nums2[index] += val
        if self.nums2[index] in self.counts:
            self.counts[self.nums2[index]] += 1
        else:
            self.counts[self.nums2[index]] = 1

    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1:
            if (tot - num) in self.counts:
                count += self.counts[tot - num]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)