class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
            heaters.sort()
            closest = [0] * len(houses)
            
            def binarySearch(target, arr):
                l, r = 0, len(arr)-1
                ans = -1
                while l <= r:
                    m = (l+r) // 2
                    if arr[m] == target:
                        return m
                    elif arr[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                    if abs(arr[m]-target) < abs(arr[ans]-target):
                        ans = m
                    elif abs(arr[m]-target) == abs(arr[ans]-target) and arr[m] < arr[ans]:
                        ans = m
                return ans
            
            for i, house in enumerate(houses):
                closest[i] = abs(house-heaters[binarySearch(house, heaters)])
            
            return max(closest)