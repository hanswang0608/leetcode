class Solution:
    # def partitionLabels(self, s: str) -> List[int]:
    #     intervals = {}
    #     ordering = []
    #     for i, c in enumerate(s):
    #         if c not in intervals:
    #             intervals[c] = [i, i]
    #             ordering.append(c)
    #         else:
    #             intervals[c] = [intervals[c][0], i]

    #     newIntervals = []
    #     prev = intervals[ordering[0]]
    #     for i in range(1, len(ordering)):
    #         cur = intervals[ordering[i]]
    #         if prev[1] < cur[0]:
    #             newIntervals.append(prev)
    #             prev = cur
    #         else:
    #             prev = [prev[0], max(prev[1], cur[1])]
    #     newIntervals.append(prev)

    #     return [ r-l+1 for l, r in newIntervals]

    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        ans = []

        l, r = 0, 0
        for i, c in enumerate(s):
            r = max(r, lastIndex[c])
            if i == r:
                ans.append(r-l+1)
                l = r+1
        return ans
        
# brute force O(n^2) -> count occurences of all chars, then for each n^2 substr, see if substr counter == total counter
# interval O(n) -> built list of intervals for each character (in order), then merge all overlapping intervals and return final length of intervals
# greedy O(n) -> build dict of lastCharIndex, for each char update end pointer to be lastCharIndex[c] if greater, and save partition when iterator reaches end

# x: [0,3]
# y: [1,4]
# z: [5,7]
# b: [6,9]
# i: [10,10]
# s: [11,11]
# l: [12,12]