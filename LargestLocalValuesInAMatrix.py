class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        res =[]
        for i in range(length-2):
            temp=[]
            for j in range(length-2):
                maxi = max(grid[i][j],grid[i][j+1],grid[i][j+2],
                           grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                           grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2])
                temp.append(maxi)
            res.append(temp)
        return res