class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c]+1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
        
# unbounded knapsack problem
# for each coin:
# 1. include ith coin and solve subproblem with same coins arr, but amount-coin
# 2. exclude ith coin and solve subproblem with coins-coin, but same amount
# f(arr, 0) = 0
# f(~arr, x) = -1
# f(arr, x<0) = -1
# f(arr, x) = min(f(arr, x-arr[0])+1, f(arr[1:], x))

# approaches:
# top-down recursive
# bottom-up tabulation 1D dp
# dp[n] -> how many coins to sum to n
# dp[0] = 0


# length of coins array? can it be empty
# value of coins (int range)
# range of amount?