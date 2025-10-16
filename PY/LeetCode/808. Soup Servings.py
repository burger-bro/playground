from functools import lru_cache
class Solution:       
    def soupServings(self, n: int) -> float:
        a = b = n     
        operations = [[100, 0],
                      [75, 25],
                      [50, 50],
                      [25, 75]]
        def dfs(a, b): 
            if a <= 0 or b <= 0:
                print("ab", a, b)
                cnt_less, cnt_equal = 0, 0
                if a<=0 and b<=0:
                    cnt_equal = 1
                elif a<=0:
                    cnt_less = 1
                all = 1
                return cnt_less, cnt_equal, all
            tmp_cnt_l, tmp_cnt_e, tmp_all = 0, 0, 0
            for i in range(4):
                n_a = a-operations[i][0]
                n_b = b-operations[i][1]
                tl, te, ta = dfs(n_a, n_b)
                tmp_cnt_l += tl
                tmp_cnt_e += te
                tmp_all += ta
            return tmp_cnt_l, tmp_cnt_e, tmp_all
        
        cnt_l, cnt_e, all = dfs(a, b)
        res = (cnt_l+0.5*cnt_e)/all
        print(cnt_l, cnt_e, all, res)
        print(7/13, 8/13, 10/13, 11/13, 12/13)
        return res

    def soupServings(self, n: int) -> float:
        a = b = n
        operations = [[100, 0],
                      [75, 25],
                      [50, 50],
                      [25, 75]]
        @lru_cache(maxsize=None)
        def dfs(a, b):
            if a <= 0 or b <= 0:
                cnt = 0
                # print("ab", a, b)
                if a<=0 and b<=0:
                    cnt = 0.5
                elif a<=0:
                    cnt = 1
                return cnt #, all
            cnt, tmp_all = 0, 0
            for i in range(4):
                n_a = a-operations[i][0]
                n_b = b-operations[i][1]
                c = dfs(n_a, n_b)
                cnt += c
            prob = cnt/4
            return prob
            # return cnt, tmp_all
        
        cnt = dfs(a, b)
        res = cnt
        print(cnt, res)
        return res


su = Solution()
# case std1
n = 50
res = su.soupServings(n)
ans = 0.62500
assert(res == ans)

# case std1
n = 100
res = su.soupServings(n)
ans = 0.71875
assert(res == ans)
