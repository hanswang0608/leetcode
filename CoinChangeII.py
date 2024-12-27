class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = [[1 if j == 0 else 0 for j in range(amount+1)] for i in range(len(coins)+1)]
        row = [0] * (amount+1)
        row[0] = 1

        for i in range(len(coins)-1, -1, -1):
            curRow = [0] * (amount+1)
            curRow[0] = 1
            for j in range(1, amount+1):
                if j - coins[i] >= 0:
                    curRow[j] += curRow[j-coins[i]]
                    # dp[i][j] += dp[i][j-coins[i]]
                curRow[j] += row[j]
                # dp[i][j] += dp[i+1][j]
            row = curRow
        
        return row[amount]

# reason with 2d dp so we move up the coins array on y axis, so permutations are not considered, but can be reduced to 1d

# coin change 1 doesn't care about permutations since each permutation gives the same number, and dp depends on min
# but for this one we do care about permutations so we are tallying