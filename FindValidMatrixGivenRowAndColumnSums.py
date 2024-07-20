class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        output = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]

        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                if rowSum[i] < colSum[j]:
                    output[i][j] = rowSum[i]
                    colSum[j] -= rowSum[i]
                    rowSum[i] = 0
                else:
                    output[i][j] = colSum[j]
                    rowSum[i] -= colSum[j]
                    colSum[j] = 0
        
        return output