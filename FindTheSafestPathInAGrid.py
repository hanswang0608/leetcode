class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        safeness = [[float('inf') for _ in range(n)] for _ in range(n)]
        queue = deque()
        # multi-source bfs with thieves as sources
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    safeness[i][j] = 0

        # calculate shortest manhattan distance from each empty grid to a thief by 
        # starting bfs from each thief
        dist = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dr, dc in directions:
                    r, c = i+dr, j+dc
                    if 0 <= r < n and 0 <= c < n and safeness[r][c] > dist:
                        queue.append((r, c))
                        safeness[r][c] = dist
            dist += 1
        
        # do a modified dijkstra's search from top left and find the best path to bottom right
        maxSafeness = [[float('-inf') for _ in range(n)] for _ in range(n)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        queue = []      # max heap
        queue.append((-safeness[0][0], 0, 0))
        maxSafeness[0][0] = safeness[0][0]
        while queue:
            _, i, j = heapq.heappop(queue)
            if visited[i][j]:
                continue
            visited[i][j] = True
            for dr, dc in directions:
                r, c = i+dr, j+dc
                if 0 <= r < n and 0 <= c < n and not visited[r][c]:
                    heapq.heappush(queue, (-safeness[r][c], r, c))
                    maxSafeness[r][c] = min(safeness[r][c], maxSafeness[i][j])
        
        return maxSafeness[n-1][n-1]
        

# brute force O(exponential) -> calculate safeness for every path, and return maximum

# multisource bfs from each thief to calculate each square's safeness factor
# modified dijkstra's from top left and find "shortest" path to bottom right, explore edge based on max safety, 
# cost of each grid is max safety achievable to reach there