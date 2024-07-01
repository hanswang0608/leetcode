class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0
        for num in arr:
            if num % 2 == 1:
                oddCount += 1
            else:
                oddCount = 0
            if oddCount == 3:
                return True
        return False