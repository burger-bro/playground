class Solution:
    def isValid(self, word: str) -> bool:
        f3, fvow, fcon = False, False, False
        vow = 'a e i o u'.split()
        vow = vow + [c.upper() for c in vow]
        print(vow)
        for c in word:
            if not (c.isdigit() or c.isalpha()):
                return False
            if c.isalpha():
                if c in vow:
                    fvow = True
                else:
                    fcon = True
        f3 = len(word) >= 3
        print(f3, fvow, fcon)
        return f3 and fvow and fcon

            
            
            

su = Solution()
# case std1
word = "AhI"
res = su.isValid(word)
ans = True
assert(res == ans)
# case std1
word = "234Adas"
res = su.isValid(word)
ans = True
assert(res == ans)
