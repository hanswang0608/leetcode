class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotated = nums[-k:] + nums[:len(nums)-k]
        # for i in range(len(nums)):
        #     nums[i] = rotated[i]
        
        copy = nums.copy()
        for i in range(len(nums)):
            nums[i] = copy[(i+len(nums)-k) % len(nums)]

        # construct a function rotate() and call it k times
        
# splice the pivot form new array