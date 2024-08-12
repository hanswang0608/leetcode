class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        d1 = {}
        d2 = Counter(s)
        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[s[i]] -= 1
            if d2[s[i]] == 0:
                del d2[s[i]]
            if len(d1) == len(d2):
                ans += 1
        return ans