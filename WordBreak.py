class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for word in wordDict:
                if i - len(word) >= 0:
                    if s[i-len(word):i] == word and dp[i-len(word)]:
                        dp[i] = True
                        break
        
        return dp[-1]

# dp[0] = True -> empty string can be made up by wordDict
# dp[n] = True if there exists a w in wordDict that s[n-len(w):n] == w && dp[n-len(w)]
# time complexity: O(SWK), S = len(s), W = len(wordDict), K = avg len of each word 