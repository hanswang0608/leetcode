class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left_arr = self.sortArray(nums[:mid])
        right_arr = self.sortArray(nums[mid:])
        l, r = 0, 0
        ans = []
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                ans.append(left_arr[l])
                l += 1
            else:
                ans.append(right_arr[r])
                r += 1
        while l < len(left_arr):
            ans.append(left_arr[l])
            l += 1
        while r < len(right_arr):
            ans.append(right_arr[r])
            r += 1
        return ans