class Solution:
    def trap(self, height: List[int]) -> int:
        highest_left = [0 for _ in range(len(height))]
        highest_right = [0 for _ in range(len(height))]

        highest_left[0] = height[0]
        for i in range(1, len(height)):
            highest_left[i] = max(height[i], highest_left[i-1])
        
        highest_right[-1] = height[-1]
        for i in reversed(range(len(height)-1)):
            highest_right[i] = max(height[i], highest_right[i+1])
        
        output = 0
        for i in range(1, len(height)-1):
            if height[i] < highest_left[i] and height[i] < highest_right[i]:
                output += min(highest_left[i], highest_right[i]) - height[i]
        
        return output
    
# this is O(n) in time and space 