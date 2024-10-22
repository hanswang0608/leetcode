class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for v, e in edges:
            adj[v].append(e)
            adj[e].append(v)

        def findCycle(v, p, visited, path):
            visited.add(v)
            path.append(v)
            for e in adj[v]:
                if e not in visited:
                    cycle = findCycle(e, v, visited, path)
                    if cycle:
                        return cycle
                else:
                    if e == p:
                        continue
                    else:
                        return path[path.index(e):]
            path.pop()
            return None
        
        cycle = findCycle(1, None, set(), [])
        cycleEdges = set()
        for i in range(len(cycle)):
            cycleEdges.add((cycle[i], cycle[i-1]))
            cycleEdges.add((cycle[i-1], cycle[i]))

        print(cycle)

        for v, e in reversed(edges):
            if (v, e) in cycleEdges:
                return [v, e]

# use DFS/backtracking to find back edge and return the nodes in the cycle
# iterate over the cycle and add edges to a set
# iterate over edges in reverse and return the first edge in the cycle
# Time Complexity: DFS:O(V+E), O(V), O(E) -> O(V+E)
# Space Complexity: O(V+E)