class Solution:
    def maxDiff(self, num: int) -> int:
        snum = str(num)
        # find none 9
        max_replace = '9'
        for c in snum:
            if c == '9':
                continue
            max_replace = c
            break
        # find none 1
        min_replace = '1'
        rr = '1'
        if snum[0] != '1':
            min_replace = snum[0]
        else:
            for c in snum:
                if c == '1' or c == '0':
                    continue
                min_replace = c
                rr = '0'
                break
        max_n = int(snum.replace(max_replace, '9'))
        min_n = int(snum.replace(min_replace, rr))
        print(max_n, min_n)
        return max_n-min_n
            

su = Solution()
# case bug
num = 1101057
res = su.maxDiff(num)
ans = 8808050
assert(res == ans)

# case bug
num = 111
res = su.maxDiff(num)
ans = 888
assert(res == ans)

# case std1
num = 555
res = su.maxDiff(num)
ans = 888
assert(res == ans)

# case std1
num = 9
res = su.maxDiff(num)
ans = 8
assert(res == ans)

# case std1
num = 123   #923 - 103
res = su.maxDiff(num)
ans = 820
assert(res == ans)
