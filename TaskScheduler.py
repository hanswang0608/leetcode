class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-f for f in freq.values()]
        heapq.heapify(heap)

        queue = deque() # (cnt, cooldown)
        time = 0
        while heap or queue:
            time += 1
            if queue:
                if queue[0][1] <= time:
                    heapq.heappush(heap, queue.popleft()[0])
            if heap:
                cnt = heapq.heappop(heap)
                if cnt + 1 != 0:
                    queue.append((cnt + 1, time + n + 1))

        return time
        
    