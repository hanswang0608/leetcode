class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    queue.append((i, j))
                    board[i][j] = '.'
        
        while queue:
            i, j = queue.popleft()
            for dr, dc in dirs:
                r, c = i+dr, j+dc
                if 0 <= r < m and 0 <= c < n and (r, c) and board[r][c] == 'O':
                    queue.append((r, c))
                    board[r][c] = '.'
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'

# 1. multi-source bfs from O's on edge of the board, 
# find all O's connected, these are not surrounded, change them to '.'
# 2. iterate over entire board and switch all O's to X's, and all '.' back to O's