class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        l = r = 0
        while r < len(nums) - 1:
            nextR = 0
            for i in range(l, r+1):
                nextR = max(nextR, i+nums[i])
            l = r + 1
            r = nextR
            ans += 1
        return ans