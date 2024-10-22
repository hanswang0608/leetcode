class Solution:
    # using quick union-find, quick because we are not using rank array to balance the trees
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # there are n=len(edges) nodes, but we do +1 to align with 1-index
        parent = [0] * (len(edges)+1)
        # set each node's parent to be itself
        # O(n)
        for i in range(len(parent)):
            parent[i] = i

        # each disjoint-set (component) has 1 representative (root of a tree)
        # recursively look for representative of the set
        # O(logn) average, O(n) worst-case for unbalanced tree, can be fixed with weighted union-find
        def find(node):
            if parent[node] == node:
                return node
            return find(parent[node])
        
        # join two disjoint-sets, with set Y being the representative
        # O(logn) average, O(n) worst
        def union(x, y):
            parent[find(x)] = parent[find(y)]


        for v, e in edges:
            # if representatives are different, then v and e are not connected, join them with union
            if find(v) != find(e):
                union(v, e)
            # if representatives are the same, then v and e are already connected
            # this is the redundant edge that will cause a cycle, return it
            else:
                return [v,e]
        

# trying union-find