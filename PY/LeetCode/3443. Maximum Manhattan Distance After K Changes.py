class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ns_max, ns_min = -float("inf"), float("inf")
        ew_max, ew_min = -float("inf"), float("inf")
        ns_cnt = 0
        ew_cnt = 0
        ans = 0
        for idx, move in enumerate(s):
            if move == 'N':
                ns_cnt += 1
            elif move == 'S':
                ns_cnt -= 1
            elif move == 'E':
                ew_cnt += 1
            elif move == 'W':
                ew_cnt -= 1
            ns_max = max(ns_max, ns_cnt)
            ns_min = min(ns_min, ns_cnt)
            ew_max = max(ew_max, ew_cnt)
            ew_min = min(ew_min, ew_cnt)

            r = max(ns_max, -ns_min) + max(ew_max, -ew_min)
            print(ns_max, -ns_min, ew_max, -ew_min)
            print(r)
            ans = min(r+2*k, idx+1)

        return ans

    # def maxDistance(self, ss: str, k: int) -> int:
    #     n, s, e, w = 0, 0, 0, 0
    #     ans = 0
    #     for idx, move in enumerate(ss):
    #         if move == 'N':
    #             n += 1
    #         elif move == 'S':
    #             s += 1
    #         elif move == 'E':
    #             e += 1
    #         elif move == 'W':
    #             w += 1

    #         mh = min(abs(n-s)+abs(e-w)+2*k, idx+1)
    #         ans = max(mh, ans)
    #     return ans

    # def maxDistance(self, ss: str, k: int) -> int:
    #     ns, ew = 0, 0
    #     ans = 0
    #     for idx, move in enumerate(ss):
    #         if move == 'N':
    #             ns += 1
    #         elif move == 'S':
    #             ns -= 1
    #         elif move == 'E':
    #             ew += 1
    #         elif move == 'W':
    #             ew -= 1

    #         mh = min(abs(ns)+abs(ew)+2*k, idx+1)
    #         ans = max(mh, ans)

    #     print(ans)
    #     return ans



su = Solution()
# case bug
s = "NSES"
k = 1
res = su.maxDistance(s, k)
ans = 4
assert(res == ans)
# case std1
s = "NWSE"
k = 1
res = su.maxDistance(s, k)
ans = 3
assert(res == ans)
# case std2
s = "NSWWEW"
k = 3
res = su.maxDistance(s, k)
ans = 6
assert(res == ans)
