from typing import List
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        lwords = {}
        for w in words:
            nw = list(w)
            snw = "".join(sorted(nw))
            if snw not in lwords:
                lwords[snw] = w
        return list(lwords.values())

    def removeAnagrams(self, words: List[str]) -> List[str]:
        while True:
            delete = -1
            for i in range(1, len(words)):
                if sorted(list(words[i])) == sorted(list(words[i-1])):
                    delete = i
                    break
            if delete != -1:
                words.pop(delete)
            else: