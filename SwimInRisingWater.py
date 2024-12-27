class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = []
        costs = [[float('inf')] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        queue.append((grid[0][0], 0, 0))    # cost to start at (0,0) is the height of (0,0)        costs[0][0] = grid[0][0]
        costs[0][0] = grid[0][0]
        while queue:
            totalCost, i, j = heapq.heappop(queue)
            if visited[i][j]:
                continue
            visited[i][j] = True
            for dr, dc in directions:
                r, c = i+dr, j+dc
                if 0 <= r < n and 0 <= c < n and not visited[r][c]:
                    # weight to move from (i,j) to (r,c) is their height difference
                    # but if (r,c) is lower or equal to (i,j), weight is 0
                    w = max(0, grid[r][c] - totalCost)  
                    if totalCost + w < costs[r][c]:
                        heapq.heappush(queue, (totalCost + w, r, c))
                        costs[r][c] = totalCost + w
        
        return costs[-1][-1]
        
# find a path to bottom right with minimum max value
# dijkstra's, where totalDistance to a node is max(totalDistance, height(node))

# 0,1,1
# 5,9,9
# 1,1,1