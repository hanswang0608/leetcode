class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left = [0] * len(nums)
        product_left[0] = 1

        for i in range(1, len(nums)):
            product_left[i] = product_left[i-1] * nums[i-1]
        
        product = 1
        output = [0] * len(nums)
        for i in reversed(range(len(nums))):
            output[i] = product_left[i] * product
            product *= nums[i]
        return output


# [1,2,4,6]
# product_left: [1,1,2,8]
# product_right: [48,24,6,1]

# [-1,0,1,2,3]
# product_left: [1,-1,0,0,0]
# product_right: [0,6,6,3,1]