class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        currentInterval = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if currentInterval[1] < intervals[i][0]:
                ans.append(currentInterval)
                currentInterval = intervals[i]
            else:
                currentInterval = [min(currentInterval[0], intervals[i][0]), 
                                    max(currentInterval[1], intervals[i][1])]
        ans.append(currentInterval)
        return ans