class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # first consider the candidate lengths have len(word)-k+1 choices
        # the range is [k, len(word)]
        # consider the max length len(word), it is word itself
        # then consider the second max length len(word)-1, 
        # it is word with one repeate char removed
        # then consider the nth max length len(word)-n,
        # it is word with one more repeate char removed after the previous one
        # here are two questions: 
        # 1.how to represent the repeate group?
        # 2.is it possible to get repeate result?
        MOD = 10**9 + 7
        repeated_groups = []
        last_char = None
        for c in word:
            if c != last_char:
                repeated_groups.append(1)
                last_char = c
            else:
                repeated_groups[-1] += 1

        def dfs(repeat, cur_len):
            if cur_len == k:
                return 0
            cur_ret = 0
            for r in range(len(repeat)):
                if repeat[r] > 1:
                    repeat[r] -= 1
                    cur_ret += dfs(repeat, cur_len-1) + 1
                    repeat[r] += 1
            print(cur_len, repeat)
            return cur_ret % MOD
        
        final_ret = dfs(repeated_groups, len(word)) + 1
        print(final_ret)
        return final_ret
                
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        repeated_groups = []
        last_char = None
        init_cnt = 1
        for c in word:
            if c != last_char:
                if init_cnt > 1:
                    repeated_groups.append(init_cnt)
                init_cnt = 1
                last_char = c
            else:
                init_cnt += 1
        if init_cnt > 1:
            repeated_groups.append(init_cnt)

        def dfs(repeat, cur_len, idx):
            if cur_len == k:
                return 0
            cur_ret = 0
            for r in range(idx, len(repeat)):
                if repeat[r] > 1:
                    repeat[r] -= 1
                    cur_ret += dfs(repeat, cur_len-1, r) + 1
                    repeat[r] += 1
            print(cur_len, repeat)
            return cur_ret % MOD
        
        final_ret = dfs(repeated_groups, len(word), 0) + 1
        print(final_ret)
        return final_ret


su = Solution()
# case TLE
# word = "aaaaaaaaagggyqgrdddddddvvvvvvtttttttttuuuuuuuuuunnnnsssssiiiiiiiiitttttuuuv"
# k = 16
# res = su.possibleStringCount(word, k)
# case std1
word = "aabbccdd"
k = 7
res = su.possibleStringCount(word, k)
ans = 5
assert(res == ans)
# case std2
word = "aabbccdd"
k = 8
res = su.possibleStringCount(word, k)
ans = 1
assert(res == ans)
# case std3
word = "aaabbb"   # aab, abb, aabb, aaab, abbb, aaabb, aabbb, aaabbb
k = 3
res = su.possibleStringCount(word, k)
ans = 8
assert(res == ans)


