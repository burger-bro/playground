from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = Counter(word)
        freq = list(d.values())
        freq.sort()
        print(freq)
        minimum = freq[0]
        del_idx = len(freq)-1
        for i in range(1, len(freq)):
            if freq[i]-minimum > k:
                del_idx = i
                break
        ans = 0
        for j in range(del_idx, len(freq)):
            print("del", j)
            ans += freq[j]-freq[del_idx-1]
        print(ans)
        return ans

    def minimumDeletions(self, word: str, k: int) -> int:
        d = Counter(word)
        freq = list(d.values())
        freq.sort()
        print(freq)
        left, right = 0, len(freq)-1
        right_cnt = 1
        left_cnt = 1
        ans = 0
        while freq[right] - freq[left] > k:
            while left < len(freq)-1 and freq[left] == freq[left+1]:
                left += 1
                left_cnt += 1
            right_del = right_cnt * (freq[right]-max(freq[right-1], (freq[left]+k)))
            left_del = left_cnt * freq[left]
            print(freq[right], freq[left])
            if right_del <= left_del:
                right_cnt += 1
                right -= 1
                ans += right_del
            else:
                left += 1
                ans += left_del
                left_cnt = 1
        print(ans)
        return ans

    def minimumDeletions(self, word: str, k: int) -> int:
        d = Counter(word)
        ans = float("inf")
        for i in range(26):
            base = chr(ord('a')+i)
            total_del = 0
            for _, v in d.items():
                if v < d[base]:
                    total_del += v
                elif v > d[base]:
                    total_del += max(v-(d[base]+k), 0)
            ans = min(ans, total_del)
        print(ans)
        return ans


su = Solution()
# case bug
word = "zzfzzzzppfp"
k = 1
res = su.minimumDeletions(word, k)
ans = 3
assert(res == ans)
# case bug
word = "klllurlrrul"
k = 1
res = su.minimumDeletions(word, k)
ans = 3
assert(res == ans)
# case 
word = "vvnowvov"
k = 2
res = su.minimumDeletions(word, k)
ans = 1
assert(res == ans)
# case 
word = "aabbcc"
k = 0
res = su.minimumDeletions(word, k)
ans = 0
assert(res == ans)
# case std1
word = "aabcaba"
k = 0
res = su.minimumDeletions(word, k)
ans = 3
assert(res == ans)
# case std2
word = "dabdcbdcdcd"
k = 2
res = su.minimumDeletions(word, k)
ans = 2
assert(res == ans)
# case std3
word = "aaabaaa"
k = 2
res = su.minimumDeletions(word, k)
ans = 1
assert(res == ans)

