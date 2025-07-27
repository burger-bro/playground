from typing import List
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        ab = {'a', 'b'}
        ret = 0
        for c in s:
            if c not in ab:
                stack.clear()
                continue
            if not stack or stack[-1] == c:
                stack.append(c)
            else:
                stack.pop()
                if c == 'b':
                    ret += x
                elif c == 'a':
                    ret += y
        print(ret)
        return ret

    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        ab = {'a', 'b'}
        ret = 0
        prefered_pattern = 'b' if x > y else 'a'

        def clear_stack(stack: List):
            nonlocal ret
            cnta = stack.count('a')
            cntb = stack.count('b')
            if cnta >= 1 and cntb >= 1:
                ret += min(cnta, cntb) * min(x, y)

        for c in s:
            if c not in ab:
                clear_stack(stack)
                stack.clear()
                continue
            if not stack or stack[-1] == c:
                stack.append(c)
            else:
                if c == prefered_pattern:
                    stack.pop()
                    ret += max(x, y)
                else:
                    stack.append(c)

        # if c == 'b':
        #     ret += x
        # elif c == 'a':
        #     ret += y
        clear_stack(stack)
        print(stack)
        print(ret)
        return ret

    def help(self):
        x = 1926
        y = 4320
        for i in range(100):
            for j in range(100):
                sss = i*x +j*y
                if sss == 108522:
                    print("output", i, j)
                elif sss == 112374:
                    print("ans", i, j)

su = Solution()
# case bug
s = "aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha"
x = 1926
y = 4320
res = su.maximumGain(s, x, y)
ans = 112374
su.help()
assert(res == ans)

# case std1
s = "cdbcbbaaabab"
x = 4
y = 5
res = su.maximumGain(s, x, y)
ans = 19
assert(res == ans)

# case std2
s = "aabbaaxybbaabb"
x = 5
y = 4
res = su.maximumGain(s, x, y)
ans = 20
assert(res == ans)

su.help()


