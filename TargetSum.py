class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, target):
            if (i, target) in cache:
                return cache[(i, target)]
            if i == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0
            cache[(i, target)] = dfs(i+1, target+nums[i]) + dfs(i+1, target-nums[i])
            return cache[(i, target)]
        return dfs(0, target)

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     s = sum(nums)
    #     # dp = [[0]*2*(s+1) for _ in range(len(nums)+1)]
    #     dp = [0]*2*(s+1)
    #     dp[target] = 1
    #     for i in range(len(nums)-1, -1, -1):
    #         newDp = [0]*2*(s+1)
    #         for j in range(-s, s+1):
    #             if j + nums[i] < s+1:
    #                 # dp[i][j] += dp[i+1][j+nums[i]]
    #                 newDp[j] += dp[j+nums[i]]
    #             if j - nums[i] >= -s:
    #                 # dp[i][j] += dp[i+1][j-nums[i]]
    #                 newDp[j] += dp[j-nums[i]]
    #         dp = newDp
    #     return dp[0]

# brute force O(2^n) -> each number can be either added or subtracted, backtrack every
# combination to see if we can reach target

# dp[i][j] = number of ways to reach target sum j with nums[i:]