class Node:
    def __init__(self, val = ""):
        self.children = OrderedDict()
        self.val = val
        self.isWord = False

class Solution:
    def insert(self, root, word):
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
        cur.isWord = True

    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        uniqueChars = set()
        for word in words:
            for c in word:
                uniqueChars.add(c)
        
        visited = set()
        cycle = set()
        topoOrder = []
        def dfs(u):
            if u in cycle:
                return True
            if u in visited:
                return False
            visited.add(u)
            cycle.add(u)
            for v in adj[u]:
                if dfs(v):
                    return True
            cycle.remove(u)
            topoOrder.append(u)

        for c in list(adj):
            if dfs(c):
                return ""

        for c in uniqueChars:
            if c not in visited:
                topoOrder.append(c)
        return "".join(topoOrder[::-1])

# O(c) -> c is total number of chars in all the words
# iterate over words to build dependency graph -> first differing char causes a dependency
# also check for invalid lexicographic ordering and return ""
# with dependency graph, do topo sort for ordering, also check for cycles
# chars with no dependency are not in dependency graph, so add them to ordering and return
        
# topo sort somehow
# need a trie to get words with prefixes?
# h -> e -> r
# r -> n


