class Solution:
    def rob(self, nums: List[int]) -> int:        
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev, cur = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
                prev, cur = cur, max(cur, prev+nums[i])
        return cur