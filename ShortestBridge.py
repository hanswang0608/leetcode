class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        n = len(grid)
        secondQueue = deque()

        # change all of islandA to be 2 instead of 1 in the grid, so they are distinct
        # also add every cell of islandA to a secondQueue, for later use
        def markFirstIsland(i, j):
            queue = deque()
            queue.append((i, j))
            while queue:
                i, j = queue.popleft()
                secondQueue.append((i, j))
                for dr, dc in directions:
                    r, c = i + dr, j + dc
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))

        # find first occurence of islandA and call BFS to mark them all as 2
        for i in range(n):
            if secondQueue:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    markFirstIsland(i, j)
                    break

        # start multi-source BFS from all cells of islandA and return distance when we reach islandB
        # traverse only to water and mark visited water with -1 so to prevent repeated visits
        # the first time encountering a value of 1 (islandB) is guaranteed to be the shortest distance
        dist = 0
        while secondQueue:
            for _ in range(len(secondQueue)):
                i, j = secondQueue.popleft()
                for dr, dc in directions:
                    r, c = i + dr, j + dc
                    if 0 <= r < n and 0 <= c < n:
                        if grid[r][c] == 0:
                            grid[r][c] = -1
                            secondQueue.append((r, c))
                        elif grid[r][c] == 1:
                            return dist
            dist += 1