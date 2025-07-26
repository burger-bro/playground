class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_replace = '9'
        min_replace = '9'
        nstr = str(num)
        for n in nstr:
            if n != '9':
                max_replace = n
                break

        for n in nstr:
            if n != '0':
                min_replace = n
                break 
        
        max_n = int(nstr.replace(max_replace, '9'))
        min_n = int(nstr.replace(min_replace, '0'))

        print(max_n - min_n)
        return max_n - min_n

su = Solution()
# case std1
num = 11891
res = su.minMaxDifference(num)
ans = 99009
assert(res == ans)

# case std1
num = 90
res = su.minMaxDifference(num)
ans = 99
assert(res == ans)
