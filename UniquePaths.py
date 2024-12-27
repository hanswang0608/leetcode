class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(1, m):
            curRow = [1] * n
            for j in range(1, n):
                curRow[j] = curRow[j-1] + row[j]
            row = curRow
        
        return row[-1]
        

# base case: final row or final column -> only 1 way to reach end
# at each square:
#   move down then calculate subproblem f(m-1, n)
#   move right then calculate subproblem f(m, n-1)
# f(1,x) = f(x,1) = 1
# f(m,n) = f(m-1,n) + f(m,n-1)

# bottom-up:
# dp[i][j] = f(i,j) = dp[i-1][j] + dp[i][j-1]

# reduce to O(N) space with 1D dp because each calculation only depends on the row below it