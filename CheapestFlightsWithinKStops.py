class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0      # represents costs to reach nodes in the previous iteration
        for _ in range(k+1):
            temp = costs.copy()
            # the order by which we iterate over edges doesn't matter
            # because each k iteration is the cost to get to a node in k stops, so if a far node is
            # checked first and can't be reached, that's a valid conclusion, and if it can be reached in k stops,
            # then we will eventually calculate it after k iterations
            for u, v, w in flights:
                if costs[u] + w < temp[v]:
                    temp[v] = costs[u] + w
            costs = temp
        return costs[dst] if costs[dst] != float('inf') else -1