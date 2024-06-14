class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev >= nums[i]:
                count += (prev + 1) - nums[i]
                prev = prev + 1
            else:
                prev = nums[i]
        return count