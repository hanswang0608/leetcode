class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # initial extra row/col to simplify index out of bounds
        # dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        row = [0] * (len(text2)+1)

        # loop from bottom right to top left
        for i in range(len(text1)-1, -1, -1):
            curRow = [0] * (len(text2)+1)
            for j in range(len(text2)-1, -1, -1):
                # if 2 front chars are equal, +1 to ans and solve subproblem with substrings of both
                if text1[i] == text2[j]:
                    # dp[i][j] = 1 + dp[i+1][j+1]
                    curRow[j] = 1 + row[j+1]
                # if front chars are not equal, ans is max of subproblems with either string
                else:
                    # dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    curRow[j] = max(row[j], curRow[j+1])
            row = curRow
        # return dp[0][0]
        return row[0]

# 2D dp because we have 2 dimensions (idx of 2 strings) to consider but space can be reduced to O(N)
# y axis (i) -> len(text1)
# x axis (j) -> len(text2)
# dp[i][j] -> subproblem(text1[i:], text2[j:])