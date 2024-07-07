class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        output = numBottles
        while numBottles // numExchange > 0:
            output += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return output