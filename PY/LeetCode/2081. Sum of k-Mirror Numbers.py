class Solution:
    def kMirror(self, k: int, n: int) -> int:
        cnt = 0
        k_digits = [str(i) for i in range(0, k)]
        k_combinations = {1: [str(i) for i in range(1, k)]}
        length = 1
        ret = 0 
        while cnt < n:
            k_palindromes = []
            if length != 1 and length//2 not in k_combinations:
                k_combinations[length//2] = []
                for c in k_combinations[length//2 - 1]:
                    for d in k_digits:
                        k_combinations[length//2].append(c + d)

            if length != 1:     
                if length % 2 == 0:
                    for p in k_combinations[length//2]:
                        k_palindromes.append(p+p[::-1])
                else:
                    for p in k_combinations[length//2]:
                        for d in k_digits:
                            k_palindromes.append(p + d + p[::-1])
            else:
                k_palindromes = k_combinations[1]

            for p in k_palindromes:
                base10 = int(p, k)
                if str(base10) == str(base10)[::-1]:
                    print(base10)
                    cnt += 1
                    ret += base10
                    if cnt == n:
                        print("ret", ret)
                        return ret
            length += 1
            print(k_palindromes)
            print(k_combinations, cnt, length)
            

        return ret

su = Solution()
# case std1
k = 2
n = 5
res = su.kMirror(k, n)
ans = 25
assert(res == ans)
# case std2
k = 3
n = 7
res = su.kMirror(k, n)
ans = 499
assert(res == ans)