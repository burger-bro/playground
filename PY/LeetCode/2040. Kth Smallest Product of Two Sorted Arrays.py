from typing import List
import heapq

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        products = []
        for num1 in nums1:
            for num2 in nums2:
                products.append(num1 * num2)
        products.sort()
        ret = products[k - 1] if k <= len(products) else -1
        print(ret)
        return ret

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pq = []
        heapq.heapify([])
        heapq.heappush(pq, (nums1[0] * nums2[0], 0, 0))
        visited = set((0, 0))
        count = 0
        while count < k:
            product, i, j = heapq.heappop(pq)
            count += 1
            if count == k:
                print(product)
                return product
            
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(pq, (nums1[i + 1] * nums2[j], i + 1, j))
                visited.add((i + 1, j))
            
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(pq, (nums1[i] * nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
    
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pq = []
        heapq.heapify([])
        if nums1[0] < 0:
            heapq.heappush(pq, (nums1[0] * nums2[-1], 0, len(nums2) - 1)) # judge
        else:
            heapq.heappush(pq, (nums1[0] * nums2[0], 0, 0))
        visited = set((0, 0))
        count = 0
        while count < k:
            product, i, j = heapq.heappop(pq)
            count += 1
            if count == k:
                print(product)
                return product
            
            j_increment = 1 if nums1[i] >= 0 else -1

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(pq, (nums1[i + 1] * nums2[j], i + 1, j))
                visited.add((i + 1, j))
            
            nxt_j = j + j_increment
            if 0 <= nxt_j < len(nums2) and (i, nxt_j) not in visited:
                if i>0 and nums1[i-1]<0 and nums1[i]>=0:
                    nxt_j = abs(len(nums2) - 1 - nxt_j)
                heapq.heappush(pq, (nums1[i] * nums2[nxt_j], i, nxt_j))
                visited.add((i, nxt_j))


su = Solution()
# case std1
nums1 = [2,5]
nums2 = [3,4]
k = 2
res = su.kthSmallestProduct(nums1, nums2, k)
ans = 8
assert(res == ans)
# case std2
nums1 = [-4,-2,0,3]
nums2 = [2,4]
k = 6
res = su.kthSmallestProduct(nums1, nums2, k)
ans = 0
assert(res == ans)
# case std3
nums1 = [-2,-1,0,1,2]
nums2 = [-3,-1,2,4,5]
k = 3
res = su.kthSmallestProduct(nums1, nums2, k)
ans = -6
assert(res == ans)
