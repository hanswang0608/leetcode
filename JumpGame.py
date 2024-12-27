class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0+nums[0]
        i = 0
        while i <= reachable:
            reachable = max(reachable, i+nums[i])
            if reachable >= len(nums) - 1:
                return True
            i += 1
        return False