class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def cost(ind: int):
            return abs(ord(s[ind])-ord(t[ind]))
        l = 0
        curCost = 0
        maxLen = 0
        for i in range(len(s)):
            curCost += cost(i)
            while curCost > maxCost:
                curCost = curCost - cost(l)
                l += 1
            maxLen = max(maxLen, i - l + 1)
        return maxLen