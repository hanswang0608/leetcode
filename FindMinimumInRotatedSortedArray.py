class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

# [3,4,5,6,1,2]

# l=0,r=5
# m=2->5

# [6,0,1,2,3,4,5]