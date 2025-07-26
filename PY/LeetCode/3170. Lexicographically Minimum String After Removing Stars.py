import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        queue = []
        heapq.heapify(queue)
        delete = []
        for idx, ch in enumerate(s):
            if ch != "*":
                heapq.heappush(queue, (ch, -idx))
            else:
                pp = heapq.heappop(queue)
                delete.append(pp[1])
        delete_set = set()
        for idx in delete:
            delete_set.add(-idx)
        ret = ""
        for idx, ch in enumerate(s):
            if idx in delete_set or ch == "*":
                continue
            else:
                ret += ch
        print(ret)
        return ret
    
su = Solution()
# case debug
s = "zzzccbbbs*"
res = su.clearStars(s)
ans = "zzzccbbs"
assert(res == ans)

# case std1
s = "aaba*"
res = su.clearStars(s)
ans = "aab"
assert(res == ans)

# case std2
s = "abc"
res = su.clearStars(s)
ans = "abc"
assert(res == ans)
