class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        bestMax = nums[0]
        for i in range(1, len(nums)):
            curMax = max(nums[i], nums[i] + curMax)
            bestMax = max(curMax, bestMax)
        return bestMax