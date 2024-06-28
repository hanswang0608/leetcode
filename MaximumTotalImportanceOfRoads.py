class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = {}
        for road in roads:
            count[road[0]] = count.get(road[0], 0) + 1
            count[road[1]] = count.get(road[1], 0) + 1

        count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

        for i, k in enumerate(count):
            count[k] = n-i
        
        output = 0
        for road in roads:
            output += count[road[0]] + count[road[1]]

        return output