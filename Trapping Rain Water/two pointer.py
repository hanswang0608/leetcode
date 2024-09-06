class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = 0
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                ans += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                ans += right_max - height[r]
        return ans

# [0,2,0,3,1,0,1,3,2,1]
# [0,0,2,2,3,3,3,3,3,3]
# [3,3,3,3,3,3,3,2,1,0]

# max_left=2, max_right=1
# l=1, r=8
