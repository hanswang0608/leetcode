class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(NlogK) because we are maintaing heap of size K but do heappush N times
        elementsFrequencyMap = Counter(nums)
        minHeap = []
        for element in elementsFrequencyMap:
            frequency = elementsFrequencyMap[element]
            heapq.heappush(minHeap, (frequency, element))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [el for freq, el in minHeap]

        # O(N + KlogN) because we heapify heap of size N and do K pops of LogN
        #
        # elementsFrequencyMap = Counter(nums)
        # maxHeap = []
        # for element in elementsFrequencyMap:
        #     frequency = elementsFrequencyMap[element]
        #     maxHeap.append((-frequency, element))
        # heapq.heapify(maxHeap)
        # ans = []
        # for i in range(min(k, len(maxHeap))):
        #     ans.append(heapq.heappop(maxHeap)[1])
        # return ans