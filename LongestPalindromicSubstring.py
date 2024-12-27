class Solution:
    def __init__(self):
        self.dp = {}
    def longestPalindrome(self, s: str) -> str:
        if s in self.dp:
            return self.dp[s]
        if s == "":
            return ""
        if len(s) == 1:
            return s
        if s[0] == s[-1]:
            inner = s[1:-1]
            ans = self.longestPalindrome(inner)
            if ans == inner:
                self.dp[s] = s
                return s
        l, r = self.longestPalindrome(s[1:]), self.longestPalindrome(s[:-1])
        if len(l) > len(r):
            self.dp[s] = l
            return l
        else:
            self.dp[s] = r
            return r

# ababd -> abab / babd
# abab -> aba / bab
# aba -> b