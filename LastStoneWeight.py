class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x-y < 0:
                heapq.heappush(stones, x-y)
        if stones:
            return -stones[0]
        else:
            return 0

# since python heapq library is minHeap, make every value negative so it behaves like a maxHeap