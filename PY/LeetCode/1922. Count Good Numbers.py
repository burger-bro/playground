class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        if n % 2 == 0:
            n_even, n_odd = n//2, n//2
        else:
            n_even, n_odd = n//2, n//2 + 1
        even_cnt = pow(5, n_even, mod=MOD)
        odd_cnt = pow(4, n_odd, mod=MOD)
        return (even_cnt * odd_cnt)%MOD
        
