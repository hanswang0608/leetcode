class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMax = curMin = 1
        for num in nums:
            temp = curMax
            curMax = max(num, curMax*num, curMin*num)
            curMin = min(num, temp*num, curMin*num)
            ans = max(ans, curMax)
        return ans