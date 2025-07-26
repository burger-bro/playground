class Node():
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        smaller_dict = {}
        for ch1, ch2 in zip(s1, s2):
            if ch1 < ch2:
                smaller_dict[ch2] = ch1
            elif ch1 > ch2:
                smaller_dict[ch1] = ch2
        print(smaller_dict)
        ret = ''
        for ch in baseStr:
            while ch in smaller_dict:
                ch = smaller_dict[ch]
            ret += ch
        print(ret)
        return ret

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(node):
            if node.parent == None:
                return node
            return find(node.parent)
        
        def merge(n1, n2):
            r1 = find(n1)
            r2 = find(n2)
            if r1 is r2: return
            if r1.val < r2.val:
                r2.parent = r1
            else:
                r1.parent = r2
        
        node_dict = {chr(i):Node(chr(i), None) for i in range(ord('a'), ord('z')+1)}
        for ch1, ch2 in zip(s1, s2):
            if ch1 == ch2: continue
            merge(node_dict[ch1], node_dict[ch2])

        ret = ""
        for ch in baseStr:
            ret += find(node_dict[ch]).val
        print(ret)
        return ret

su = Solution()
# case bug
s1 = "aabbbabbbbbabbbbaabaabbaaabbbabaababaaaabbbbbabbaa"
s2 = "aabbaabbbabaababaabaababbbababbbaaaabbbbbabbbaabaa"
baseStr = "buqpqxmnajphtisernebttymtrydomxnwonfhfjlzzrfhosjct"
res = su.smallestEquivalentString(s1, s2, baseStr)
ans = "makkek"
assert(res == ans)

# case std1
s1 = "parker"
s2 = "morris"
baseStr = "parser"
res = su.smallestEquivalentString(s1, s2, baseStr)
ans = "makkek"
assert(res == ans)

# case std2
s1 = "hello"
s2 = "world"
baseStr = "hold"
res = su.smallestEquivalentString(s1, s2, baseStr)
ans = "hdld"
assert(res == ans)

# case std3
s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
res = su.smallestEquivalentString(s1, s2, baseStr)
ans = "aauaaaaada"
assert(res == ans)