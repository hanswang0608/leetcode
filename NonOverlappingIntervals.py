class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[0])
        prevEnd = intervals[0][1]
        ans = 0
        for start, end in intervals[1:]:
            if start < prevEnd:
                ans += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return ans