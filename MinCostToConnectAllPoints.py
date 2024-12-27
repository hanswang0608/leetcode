class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        queue = []
        visited = set()
        key = [float('inf')] * len(points)
        mstCost = 0

        # build undirected connected graph all points, with manhattan distance as weight
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        # prim's algo
        queue.append((0, 0))
        key[0] = 0
        while queue:
            cost, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            mstCost += cost
            for neighbor, dist in adj[node]:
                if neighbor not in visited and dist < key[neighbor]:
                    key[neighbor] = dist
                    heapq.heappush(queue, (dist, neighbor))
        
        return mstCost