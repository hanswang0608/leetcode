class Solution:
    def minimumDeletions(self, s: str) -> int:
        dpA = [0] * (len(s)+1)
        dpB = [0] * (len(s)+1)
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'a':
                dpA[i] = min(dpA[i+1], dpB[i+1])
                dpB[i] = 1+dpB[i+1]
            elif s[i] == 'b':
                dpA[i] = 1+dpA[i+1]
                dpB[i] = dpB[i+1]
        return min(dpA[0], dpB[0])

# brute force O(n*2^n) -> build every possible subsequence and check if its balanced

# dp O(n)

# abbbaab

# dpA[i] -> num deletions to make substring balanced with A as first char
# dpB[i] -> num deletions to make substring balanced with B as first char
# if s[i] == 'a':
# dpA[i] = min(dpA[i+1], dpB[i+1])
# dpB[i] = 1+dpB[i+1]
# if s[i] == 'b':
# dpA[i] = 1+dpA[i+1]
# dpB[i] = dpB[i+1]
# ans = min(dpA[0], dpB[o])