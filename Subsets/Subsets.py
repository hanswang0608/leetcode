class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(nums, path):
            output.append(path)
            if not nums:
                return
            else:
                for i in range(len(nums)):
                    dfs(nums[i+1:], path + [nums[i]])

        dfs(nums, [])
        return output