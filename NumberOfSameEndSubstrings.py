from collections import defaultdict


class Solution:
    def numSameEnd(self, s, queries):
        prefixCharCount = defaultdict(lambda: [0] * (len(s)+1))

        for i, c in enumerate(s):
            prefixCharCount[c][i+1] = prefixCharCount[c][i] + 1
            for key in prefixCharCount:
                if key == c:
                    continue
                prefixCharCount[key][i+1] = prefixCharCount[key][i]
        
        sameEnd = [[ 1 if i==j else 0 for j in range(len(s))] for i in range(len(s))]

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                sameEnd[i][j] = sameEnd[i][j-1] + (prefixCharCount[s[j]][j] - prefixCharCount[s[j]][i]) + 1
        
        return[ sameEnd[l][r] for l, r in queries]

sol = Solution()
print(sol.numSameEnd("abcaab", [[0,0],[1,4],[0,5]]))