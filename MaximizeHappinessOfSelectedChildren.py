from heapq import _heapify_max, _heappop_max

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        _heapify_max(happiness)
        sum = 0
        for i in range(k):
            num = _heappop_max(happiness) - i
            if num > 0:
                sum += num
            else:
                break
        return sum