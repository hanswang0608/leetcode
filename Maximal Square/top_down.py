from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = [[None]*n for _ in range(m)]
        
        def maxSquareLength(r, c):
            if cache[r][c] is not None:
                return cache[r][c]
            if matrix[r][c] == '0':
                return 0
            elif r == m-1 or c == n-1:
                return 1
            cache[r][c] = min(maxSquareLength(r, c+1), maxSquareLength(r+1, c+1), maxSquareLength(r+1, c)) + 1
            return cache[r][c]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, maxSquareLength(i, j))
        return ans**2