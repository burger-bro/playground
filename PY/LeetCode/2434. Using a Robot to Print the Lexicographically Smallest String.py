class Solution:
    def robotWithString(self, s: str) -> str:
        smaller = [-1]*len(s)
        small = "z"
        s_idx = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] < small:    
                small = s[i]
                s_idx = i
            else:
                smaller[i] = s_idx
        print(smaller)

        stack = []
        ret = ""
        for i in range(0, len(s)):
            print(stack)
            stack.append(i)
            while stack and smaller[stack[-1]] <= i:
                ret += s[stack.pop()]
        print(ret)
        return ret

    def robotWithString(self, s: str) -> str:
        smaller = [-1]*len(s)
        small = "z"
        s_idx = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] < small:    
                small = s[i]
                s_idx = i
            elif s[i] != small:
                smaller[i] = s_idx
        print(smaller)

        stack = [0]
        ret = ""
        for i in range(1, len(s)):
            print(stack)
            # while stack and smaller[stack[-1]] <= i:
            #     ret += s[stack.pop()]
            while stack and smaller[stack[-1]] <= i and s[i] > s[stack[-1]]:
                ret += s[stack.pop()]
            stack.append(i)
        
        print(stack)
        for c in stack[::-1]:
            ret += s[c]
        print(ret)
        return ret

    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter

        freq = Counter(s)
        st = []
        res = []
        
        def min_char(freq):
            for i in range(26):
                ch = chr(ord('a') + i)
                if freq[ch] > 0:
                    return ch
            return 'a'

        for ch in s:
            st.append(ch)
            freq[ch] -= 1
            while st and st[-1] <= min_char(freq):
                res.append(st.pop())

        while st:
            res.append(st.pop())

        return ''.join(res)

su = Solution()
# case bug2
s = "mmuqezwmomeplrtskz"
res = su.robotWithString(s)
ans = "eekstrlpmomwzqummz"
assert(res==ans)

# case bug
s = "bydizfve"
res = su.robotWithString(s)
ans = "bdevfziy"
assert(res==ans)

# case std1
s = "zza"
res = su.robotWithString(s)
ans = "azz"
assert(res==ans)
# case std2
s = "bac"
res = su.robotWithString(s)
ans = "abc"
assert(res==ans)
# case std3
s = "bdda"
res = su.robotWithString(s)
ans = "addb"
assert(res==ans)
