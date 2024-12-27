class Solution:
    # BFS, kinda like bellman ford with a queue
    # O(V*E)
    # def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    #     adj = defaultdict(list)
    #     queue = deque()
    #     lowestCost = [float('inf')] * (n+1)
    #
    #     for u, v, w in times:
    #         adj[u].append((v, w))
    #
    #     queue.append(k)
    #     lowestCost[k] = 0
    #     while queue:
    #         u = queue.popleft()
    #         cost = lowestCost[u]
    #         for v, w in adj[u]:
    #             if cost + w < lowestCost[v]:
    #                 lowestCost[v] = cost + w
    #                 queue.append(v)
    #
    #     ans = max(lowestCost[1:])
    #     return ans if ans != float('inf') else -1
    

    # djikstra's
    # O(ElogV)
    # basically bfs but with a minheap / priority queue
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        queue = []
        visited = set()
        highestCost = 0

        for u, v, w in times:
            adj[u].append((v, w))

        queue.append((0, k))
        while queue:
            cost, u = heapq.heappop(queue)
            if u in visited:
                continue
            visited.add(u)
            highestCost = max(highestCost, cost)
            for v, w in adj[u]:
                if v not in visited:
                    heapq.heappush(queue, (cost + w, v))

        return highestCost if len(visited) == n else -1
