from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n+1)
        ans = 0

        for i in range(m-1, -1, -1):
            newDp = [0] * (n+1)
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '0':
                    # dp[i][j] = 0
                    newDp[j] = 0
                else:
                    # dp[i][j] = min(dp[i][j+1], dp[i+1][j+1], dp[i+1][j]) + 1
                    # ans = max(ans, dp[i][j])
                    newDp[j] = min(newDp[j+1], dp[j+1], dp[j]) + 1
                    ans = max(ans, newDp[j])
            dp = newDp
        
        return ans**2