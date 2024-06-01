class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        def fliprow(grid, r):
            for i in range(len(grid[r])):
                if grid[r][i] == 0:
                    grid[r][i] = 1
                else:
                    grid[r][i] = 0
        def flipcol(grid, c):
            for i in range(len(grid)):
                if grid[i][c] == 0:
                    grid[i][c] = 1
                else:
                    grid[i][c] = 0

        for r in range(len(grid)):
            if grid[r][0] == 0:
                fliprow(grid, r)
        for c in range(1, len(grid[0])):
            num_ones = 0
            for r in range(len(grid)):
                if grid[r][c] == 1:
                    num_ones += 1
            if num_ones <= len(grid)//2:
                flipcol(grid, c)
        
        score = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                score += grid[i][j] * 2**(len(grid[0])-1-j)

        return score