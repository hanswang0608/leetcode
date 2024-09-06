class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search for row first
        u, d = 0, len(matrix)-1
        row = None
        while u <= d:
            m = (u+d) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif matrix[m][-1] < target:
                u = m + 1
            else:
                d = m - 1
        if row is None:
            return False
        
        # found correct row, search within row
        l, r = 0, len(matrix[row])-1
        while l <= r:
            m = (l+r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False