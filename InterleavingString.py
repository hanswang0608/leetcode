class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = defaultdict(bool)
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(s1) and j == len(s2):
                return True
            if i < len(s1):
                cache[(i, j)] = (s1[i] == s3[i+j] and dfs(i+1, j))
            if j < len(s2):
                cache[(i, j)] = cache[(i, j)] or (s2[j] == s3[i+j] and dfs(i, j+1))
            return cache[(i, j)]
        return dfs(0, 0)

    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     if len(s1) + len(s2) != len(s3):
    #         return False
    #     dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
    #     dp[-1][-1] = True
    #     for i in range(len(s1), -1, -1):
    #         for j in range(len(s2), -1, -1):
    #             if i < len(s1):
    #                 dp[i][j] = s1[i] == s3[i+j] and dp[i+1][j]
    #             if j < len(s2):
    #                 dp[i][j] = dp[i][j] or s2[j] == s3[i+j] and dp[i][j+1]
    #     print(dp)
    #     return dp[0][0]
        
# 3:49

# brute force O(2^n) -> try building s3 by every possible interleaving combination

# dp[i][j] = is it possible to build s3[i+j:] using s1[i] and s2[j]

# base case:
# i==len(s1) and j==len(s1) -> return True since we used every letter
# at any point if s1[i] != s3[i+j] and s2[j] != s3[i+j] return False

# recurrence relation:
# dp[i][j] = (s1[i] == s3[i+j] and dp[i+1][j]) or (s2[j] == s3[i+j] and dp[i][j+1])