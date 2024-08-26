class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])-1
                    if rows[i][num] or cols[j][num] or boxes[i//3][j//3][num]:
                        return False
                    else:
                        rows[i][num] = True
                        cols[j][num] = True
                        boxes[i//3][j//3][num] = True
        
        return True

# brute force -> whenever a number is encountered, iterate over its row/col/box to see if valid
# keep set/array to denote if a row/col/box already has a certain number