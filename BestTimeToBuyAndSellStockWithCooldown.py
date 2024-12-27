class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0] * len(prices)
        sell = [0] * len(prices)
        sell[-1] = prices[-1]
        for i in range(len(profit)-2, -1, -1):
            sellToday = prices[i] + (profit[i+2] if i+2 < len(prices) else 0)
            sell[i] = max(sellToday, sell[i+1])
            profit[i] = max(-prices[i] + sell[i+1], profit[i+1])
        return profit[0]

# decision at anyday
# buy on day i: profit = max(sell on any day j>i + profit(day j+2))
# don't buy on day i: profit = profit(day i+1)

# dp[0] = 0
# dp[i] = max(-prices[i] + max(prices[j] + dp[j+2]), dp[i+1])

# optimize by using another dp array to store max(prices[j] + dp[j+2]) as sell[j] to 
# reduce time complexity to linear