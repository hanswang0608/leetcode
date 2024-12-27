class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            # if the sum is odd, sum/2 is not an int and no subset can sum to it
            return False
        target = total // 2

        # dp[i][j] -> if j can be summed to using nums[i:]
        dp = [[True if j == 0 else False for j in range(target+1)] for i in range(len(nums)+1)]

        for i in reversed(range(len(nums))):
            for j in range(1, target+1):
                if j-nums[i] >= 0:
                    dp[i][j] = dp[i+1][j-nums[i]]
                dp[i][j] = dp[i][j] or dp[i+1][j]
        return dp[0][target]


# for 2 subsets to be equal, they both must sum to sum(nums)/2
# so target = sum(nums)/2
# we have 2^n subsets, and we can use brute-force backtracking to explore every possible subset
# and return True if any subset sums to target
# but I wonder if we have a better approach than brute-force
# subsets are not neccesarily contiguous, so sliding window cannot be used
# that leaves us with dp for optimizing
# this can be reduced to a problem of 0/1 knapsack summing to target

# dp[:][0] = True -> target of 0 can be achieved by not using any numbers
# dp[i][j] = dp[i+1][j-nums[i]] or dp[i+1][j]

# nums cant be 0?
# size of nums
# subsets can be non-contiguous? so not subarrays