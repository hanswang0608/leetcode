class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        l = len(nums)-1
        while l > 0:
            if nums[l-1] < nums[l]:
                r = l
                while r < len(nums)-1:
                    if nums[r] > nums[l-1] and nums[r+1] <= nums[l-1]:
                        break
                    r += 1
                nums[l-1], nums[r] = nums[r], nums[l-1]
                nums[l:] = nums[-1:l-1:-1]
                return
            l -= 1
        nums[:] = nums[::-1]