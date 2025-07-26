class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        target_len = len(word)-numFriends+1
        max_string = "a" * target_len
        for i in range(len(word)-target_len+1):
            if word[i:i+target_len] > max_string:
                max_string = word[i:i+target_len]
        print(max_string)
        return max_string

    def answerString(self, word: str, numFriends: int) -> str:
        cur_max_char = 'a'
        char_idx = []
        for i, ch in enumerate(word):
            if ch > cur_max_char:
                cur_max_char = ch
                char_idx = []
            if ch == cur_max_char:
                char_idx.append(i)
        print(char_idx)

        max_len = len(word)-numFriends+1
        ret = word[char_idx[0]]
        cnt = 1
        while True:
            print("ret", ret)
            if cnt >= max_len:
                break
            tmp_idx = []
            cur_max_char = 'a'
            for idx in char_idx:
                if idx+1>=len(word):
                    # 停止条件？
                    continue
                if word[idx+1] > cur_max_char:
                    cur_max_char = word[idx+1]
                    tmp_idx = []
                if word[idx+1] == cur_max_char:
                    tmp_idx.append(idx+1)
            cnt += 1
            char_idx = tmp_idx
            if not char_idx:
                break
            ret += word[char_idx[0]]
        print(ret)
        return ret
    
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word
        res = ""
        length = len(word) - numFriends + 1
        for i in range(0, len(word)):
            temp = word[i : i + length]
            if temp > res:
                res = temp
        return res

su = Solution()
# case bug
word = "gh"
numFriends = 1
res = su.answerString(word, numFriends)
ans = "gh"
assert(res == ans)

# case bug
word = "aann"
numFriends = 2
res = su.answerString(word, numFriends)
ans = "nn"
assert(res == ans)

# case std1
word = "dbca"
numFriends = 2
res = su.answerString(word, numFriends)
ans = "dbc"
assert(res == ans)
# case std2
word = "gggg"
numFriends = 4
res = su.answerString(word, numFriends)
ans = "g"
assert(res == ans)
