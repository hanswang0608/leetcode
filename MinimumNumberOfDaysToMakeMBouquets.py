from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < k*m:
            return -1
        uniqueBloomDates = set(bloomDay)
        datesSorted = sorted(list(uniqueBloomDates))

        def canMakeBouquets(date):
            numBouquets = 0
            groupLen = 0
            for rose in bloomDay:
                if rose <= date:
                    groupLen += 1
                else:
                    groupLen = 0
                if groupLen >= k:
                    numBouquets += 1
                    groupLen = 0
                if numBouquets >= m:
                    return True
            return False
        
        left, right = 0, len(datesSorted)-1
        while left <= right:
            mid = (left + right) // 2
            if canMakeBouquets(datesSorted[mid]):
                right = mid - 1
            else:
                left = mid + 1
        return datesSorted[left]