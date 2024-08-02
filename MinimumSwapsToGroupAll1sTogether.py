class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        numOnes = 0
        curMoves = 0
        minMoves = len(nums)

        for num in nums:
            if num == 1:
                numOnes += 1
        
        for i in range(numOnes):
            if nums[i] == 0:
                curMoves += 1

        l, r = 0, numOnes-1
        while l < len(nums):
            minMoves = min(minMoves, curMoves)
            r = (r+1) % len(nums)
            if r != numOnes-1:
                if nums[r] == 0:
                    curMoves += 1
                if nums[l] == 0:
                    curMoves -= 1
            l += 1
        
        return minMoves