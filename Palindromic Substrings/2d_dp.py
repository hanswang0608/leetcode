class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[True if i >= j else False for j in range(len(s))] for i in range(len(s))]
        ans = len(s)
        for i in reversed(range(len(s)-1)):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans += 1
        return ans

# dp[i][j] -> s[i:j+1] is a palindrome
# return # of True entries in dp as ans

# s is a palindrome if s[0] == s[-1] and s[1:-1] (stored as dp[i][j]) is a palindrome
# check diagonally down and left in the dp table for if s[1:-1] is palindrome
# tabulate from bottom to up, left to right