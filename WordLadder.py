class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        diffByOne = {}
        for word in wordList:
            diffByOne[word] = self.precompute(word)

            
        graph = defaultdict(list)
        
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if wordList[i] in diffByOne[wordList[j]]:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        
        queue = deque()
        queue.append((endWord, 1))
        visited = defaultdict(bool)
        visited[endWord] = True
        ans = float('inf')

        while queue:
            cur, dist = queue.popleft()
            if beginWord in diffByOne[cur]:
                ans = min(ans, dist+1)
            for neighbor in graph[cur]:
                if not visited[neighbor]:
                    queue.append((neighbor, dist+1))
                    visited[neighbor] = True

        return ans if ans != float('inf') else 0

    def precompute(self, word):
        output = set()
        for k in range(len(word)):
            pre = word[:k]
            post = word[k+1:]
            for i in range(26):
                output.add(pre + chr(ord('a')+i) + post)
        return output

# 1. build graph between words -> O(N^2)
# 2. start BFS from endWord and check if each word is 1 away from beginWord
