class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowMins = [float('inf') for _ in range(len(matrix))]
        colMaxs = [0 for _ in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] < rowMins[r]:
                    rowMins[r] = matrix[r][c]
                if matrix[r][c] > colMaxs[c]:
                    colMaxs[c] = matrix[r][c]
        
        return set(rowMins).intersection(set(colMaxs))