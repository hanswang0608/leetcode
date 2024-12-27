class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up dp with tabulation -> keep results of subproblems
        #
        # dp = [0] * (len(cost)+1)
        # for i in range(2, len(dp)):
        #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # return dp[-1]

        # bottom up constant space -> only keep values needed for next calculation
        prev, cur = 0, 0
        for i in range(2, len(cost)+1):
            prev, cur = cur, min(cur+cost[i-1], prev+cost[i-2])
        return cur

# f(0) = 0
# f(1) = 0
# f(2) = min(f(1)+cost[1], f(0)+cost[0]) = min(2,1) = 1
# f(3) = min(f(2)+cost[2], f(1)+cost[1]) = min(1+3,2) = 2
# f(n) = min(f(n-1)+cost[n-1], f(n-2)+cost[n-2])
# cur = f(n-1), prev = f(n-2)