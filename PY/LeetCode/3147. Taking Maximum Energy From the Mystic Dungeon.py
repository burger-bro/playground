from typing import List

def ifprint(msg, case):
    if case == 0:
        print(msg)

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        NINF = -float("inf")
        dp = [NINF]*n
        for i in range(n-1, -1, -1):
            acc = 0
            idx = i
            ifprint(f"{dp}", i)
            while idx < n:
                ifprint(f"{acc} {dp} {idx}", i)
                if dp[idx] > NINF:
                    acc += dp[idx]
                    break
                acc += energy[idx]
                idx += k
            dp[i] = max(dp[i], acc)
        print(dp)
        return max(dp)
    
su = Solution()
# case std1
energy = [5,2,-10,-5,1]
k = 3
ans = 3
res = su.maximumEnergy(energy, k)
assert(res == ans)


