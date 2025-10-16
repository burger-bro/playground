class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = 0
        empty = 0
        while numBottles > numExchange:
            cnt += numBottles
            empty += numBottles
            div = empty // numExchange
            empty -= div * numExchange
            numBottles = div
        return cnt + numBottles
