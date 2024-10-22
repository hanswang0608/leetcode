class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        ans = 0

        def dfs(row, col, visited):
            visited.add((row, col))
            ret = 1
            for dr, dc in dirs:
                r, c = row + dr, col + dc
                if 0 <= r < n and 0 <= c < m and (r, c) not in visited and grid[r][c] == 1:
                    ret += dfs(r, c, visited)
            return ret

        visited = set()
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == 1:
                    ans = max(dfs(i, j, visited), ans)

        return ans