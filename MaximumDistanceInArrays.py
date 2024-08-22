class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest, largest = 0, 0
        for i in range(1, len(arrays)):
            if arrays[i][0] < arrays[smallest][0]:
                smallest = i
            if arrays[i][-1] > arrays[largest][-1]:
                largest = i
        
        if smallest != largest:
            return arrays[largest][-1] - arrays[smallest][0]
        
        secondSmallest, secondLargest = None, None
        for i in range(len(arrays)):
            if i != smallest and (secondSmallest is None or arrays[i][0] < arrays[secondSmallest][0]):
                secondSmallest = i
            if i != largest and (secondLargest is None or  arrays[i][-1] > arrays[secondLargest][-1]):
                secondLargest = i
        
        return max(arrays[largest][-1] - arrays[secondSmallest][0], arrays[secondLargest][-1] - arrays[smallest][0])
# [[1,2,3],[4,5],[1,2,3]]
# [1,4,1]
# [3,5,3]

# [[1,10],[4,5],[3,7]]
# [1,4,3]
# [10,5,7]

# [[1,10],[4,7],[3,5]]
# [1,4,3]
# [10,7,5]