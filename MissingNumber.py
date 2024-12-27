class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        return int(n*(n-1)/2) - sum(nums)