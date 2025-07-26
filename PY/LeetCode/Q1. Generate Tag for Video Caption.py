from typing import List
class Solution:
    def generateTag(self, caption: str) -> str:
        words: List[str] = []
        tag = ['#']
        first_flag = True
        for ch in caption:
            if ch == ' ' and words:
                tag.extend(words)
                words = []
                first_flag = False
            if ch.isalpha():
                ch = ch.lower()
                if not first_flag and not words:
                    ch = ch.capitalize()
                words.append(ch)
        tag.extend(words)
        tag = tag[:100]
        ret = "".join(tag)
        print(ret)
        return ret
        

su = Solution()
# case std1
caption = "Leetcode daily streak achieved"
res = su.generateTag(caption)
ans =  "#leetcodeDailyStreakAchieved"
assert(res == ans)
