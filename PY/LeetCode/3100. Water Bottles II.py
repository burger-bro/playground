class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        cnt = 0
        empty = 0
        while numBottles > numExchange:
            cnt += numBottles
            empty += numBottles
            numBottles = 0
            while empty >= numExchange:
                empty -= numExchange
                numBottles += 1
                numExchange += 1
        if numBottles:
            cnt += numBottles
            empty += numBottles
            while empty >= numExchange:
                empty -= numExchange
                cnt += 1
                numExchange += 1
        return cnt