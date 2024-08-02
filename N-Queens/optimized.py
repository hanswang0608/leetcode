from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)]  for _ in range(n)]  # board state
        rows, cols = [True] * n, [True] * n                   # whether each row/col is occupied by a queen
        r_diag, l_diag = [True] * (n*2-1), [True] * (n*2-1)   # whether each diagonal is occupied by a queen, r_diag=pos slope, l_diag=neg slope
        ans = []

        # At each square (r, c), 2 decisions are made
        #   1. If safe, place a queen and move to next row
        #   2. Skip it, check remaining columns
        def backtrack(r, numQueens):
            # save solution when enough queens are placed
            if numQueens == n:
                ans.append([''.join(row) for row in board])
                return

            if r == n:
                return

            for c in range(n):
                if self.isSafe(r, c, rows, cols, r_diag, l_diag):
                    # place queen at (r, c)
                    self.update(r, c, rows, cols, r_diag, l_diag, False)
                    board[r][c] = 'Q'
                    numQueens += 1

                    # explore branch of decision tree where a queen is placed at (r, c), continue to next row
                    backtrack(r+1, numQueens)

                    # remove queen from (r, c) -> "pop" after backtracking
                    self.update(r, c, rows, cols, r_diag, l_diag, True)
                    board[r][c] = '.'
                    numQueens -= 1

        backtrack(0, 0)
        return ans

    # check if a square is safe
    def isSafe(self, r, c, rows, cols, r_diag, l_diag):
        return rows[r] and cols[c] and r_diag[r+c] and l_diag[r-c+len(rows)-1]
    
    # update board safety state
    # safe=True -> remove a queen from (r, c), needed when "popping" after backtracking
    # safe=False -> place a queen at (r, c)
    def update(self, r, c, rows, cols, r_diag, l_diag, safe):
        rows[r] = safe
        cols[c] = safe
        r_diag[r+c] = safe
        l_diag[r-c+len(rows)-1] = safe
        

sol = Solution()

print(sol.solveNQueens(4))