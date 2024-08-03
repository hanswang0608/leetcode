class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [True for _ in range(len(s))]
        prev = dp[:]
        ans = len(s)
        for i in reversed(range(len(s)-1)):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and prev[j-1]:
                    dp[j] = True
                    ans += 1
                else:
                    dp[j] = False
            prev = dp.copy()
        return ans

# dp[i][j] -> s[i:j+1] is a palindrome
# return # of True entries in dp as ans

# s is a palindrome if s[0] == s[-1] and s[1:-1] (stored as dp[i][j]) is a palindrome
# check diagonally down and left in the dp table for if s[1:-1] is palindrome
# tabulate from bottom to up, left to right

# simplify to be O(n) space complexity
# each calculation only needs diagonally prev value, so keeping only the last row of dp is enough
# use prev to store dp values of last row, and write new values to dp