class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        memo = [[0 for _ in range(n)] for _ in range(m) ]

        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            longest = 1
            for dr, dc in directions:
                r, c = i+dr, j+dc
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > matrix[i][j]:
                    longest = max(1+dfs(r, c), longest)
            memo[i][j] = longest
            return longest

        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(dfs(i, j), ans)

        return ans

        
# naive solution -> dfs from every cell
# memoize longest path from each cell within dfs