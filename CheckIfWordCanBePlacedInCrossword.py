class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == ' ' or board[i][j] == word[0]:
                    queue.append((i, j))
        
        def search(i, j, dr, dc, k):
            r, c = i + dr, j + dc
            if k == len(word)-1:
                if not (0 <= r < m and 0 <= c < n) or board[r][c] == '#':
                    return True
                else:
                    return False
            elif k < len(word)-1:
                if not (0 <= r < m and 0 <= c < n) or board[r][c] == '#' or (board[r][c] != ' ' and board[r][c] != word[k+1]):
                    return False
            return search(r, c, dr, dc, k+1)
        
        while queue:
            i, j = queue.pop()
            for dr, dc in dirs:
                r, c = i-dr, j-dc
                if 0 <= r < m and 0 <= c < n and board[r][c] != '#':
                    continue
                if search(i, j, dr, dc, 0):
                    return True
        
        return False
