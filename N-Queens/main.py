from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)]  for _ in range(n)]  # board state
        rows, cols = [0] * n, [0] * n
        r_diag, l_diag = [0] * (n*2-1), [0] * (n*2-1)
        ans = []
        calls = 0


        # At each square (r, c), 2 decisions can be made:
        #   1. If safe, place a queen
        #   2. Skip it
        def backtrack(r, c, numQueens):
            # save solution when enough queens are placed
            if numQueens == n:
                ans.append([''.join(row) for row in board])
                return

            if r == n or c == n:
                return
            
            nonlocal calls
            calls += 1

            nr, nc = r, c
            while nr < n and nc < n:
                lr, lc = nr, nc
                nr, nc = self.getNextPos(nr, nc, n)
                if self.isSafe(lr, lc, rows, cols, r_diag, l_diag):
                    # place queen at (lr, lc)
                    self.update(lr, lc, rows, cols, r_diag, l_diag, 1)
                    board[lr][lc] = 'Q'
                    numQueens += 1
                    
                    # explore branch of decision tree where a queen is placed at (nr, nc)
                    backtrack(nr, nc, numQueens)

                    # remove queen from (nr, nc) -> "pop" after backtracking
                    self.update(lr, lc, rows, cols, r_diag, l_diag, -1)
                    board[lr][lc] = '.'
                    numQueens -= 1

            
            # nr, nc = self.getNextPos(r, c, n)

            # if self.isSafe(r, c, rows, cols, r_diag, l_diag):
            #     # place queen at (r, c)
            #     self.update(r, c, rows, cols, r_diag, l_diag, 1)
            #     board[r][c] = 'Q'
            #     numQueens += 1
                
            #     # explore branch of decision tree where a queen is placed at (r, c)
            #     backtrack(nr, nc, numQueens)

            #     # remove queen from (r, c) -> "pop" after backtracking
            #     self.update(r, c, rows, cols, r_diag, l_diag, -1)
            #     board[r][c] = '.'
            #     numQueens -= 1
                

            # explore outcomes where a queen is not placed at (r, c)
            backtrack(nr, nc, numQueens)

        backtrack(0, 0, 0)
        print(calls)
        return ans
    
    # helper function for iterating through the squares
    def getNextPos(self, r, c, n):
        new = r * n + c + 1
        nr, nc = new // n, new % n
        return (nr, nc)

    def isSafe(self, r, c, rows, cols, r_diag, l_diag):
        return rows[r] == 0 and cols[c] == 0 and r_diag[r+c] == 0 and l_diag[r-c+len(rows)-1] == 0
    
    # update board safety state
    # include=1 -> place a queen at (r, c)
    # include=-1 -> remove a queen from (r, c), needed when "popping" after backtracking
    def update(self, r, c, rows, cols, r_diag, l_diag, include):
        rows[r] += include
        cols[c] += include
        r_diag[r+c] += include
        l_diag[r-c+len(rows)-1] += include
        

sol = Solution()

print(sol.solveNQueens(9))