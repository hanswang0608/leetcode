class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(left, right, s):
            if len(s) == n * 2:
                ans.append(s)
                return
            if left < n:
                dfs(left+1, right, s+'(')
            if right < left:
                dfs(left, right+1, s+')')
        dfs(0, 0, "")
        return ans

# brute force O(n*2^n)-> n pairs = string of length 2n -> generate every possible string of length 2n where each char can be either
# ( or ) and check if the string is valid