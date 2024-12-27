class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(intervals)):
            l1, r1 = intervals[i]
            l2, r2 = newInterval
            if r2 < l1:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif r1 < l2:
                ans.append([l1, r1])
            else:
                newInterval = [min(l1, l2), max(r1, r2)]
                    
        ans.append(newInterval)
        return ans

# iterate interviews from left to right