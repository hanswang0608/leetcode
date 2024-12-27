class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev, cur = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            prev, cur = cur, max(cur, prev+nums[i])
        
        return cur
# f(0) = nums[0]
# f(1) = max(nums[0], nums[1])
# f(2) = max(f(1), f(0)+nums[2])
# f(n) = max(f(n-1), f(n-2)+nums[n]) -> two prev values need to be in memory as prev and cur