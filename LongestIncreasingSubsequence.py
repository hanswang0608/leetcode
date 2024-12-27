class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        longest = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    longest = max(longest, dp[i])
        return longest

# dp[i] -> longest subsequence involving nums[i]
# this is a case where to calculate dp[i], we need another loop over all prev dp values
# O(N^2) compared to usual O(N) 1D dp, which is tricky
# remember that if O(N) seems impossible, try O(N^2)
# don't just aim for the best complexity right away

# this can actually be done in nlogn!