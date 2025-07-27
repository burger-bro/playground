class Solution:
    def possibleStringCount(self, word: str) -> int:
        last = None
        possible_count = 1
        for c in word:
            if c == last:
                possible_count += 1
            last = c
        return possible_count