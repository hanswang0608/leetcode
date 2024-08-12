class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        numOdds = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        ans = 0
        for num in nums:
            numOdds += num % 2
            if numOdds - k in prefixSum:
                ans += prefixSum[numOdds - k]
            prefixSum[numOdds] += 1
        return ans

# most naive brute force -> n^3
# optimized brute force -> n^2
# sliding window -> n