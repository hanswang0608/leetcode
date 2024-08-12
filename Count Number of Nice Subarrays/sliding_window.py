class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIndices = deque()
        ans = 0
        lastPopped = -1
        leftGap = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                oddIndices.append(i)
            if len(oddIndices) > k:
                lastPopped = oddIndices.popleft()
            if len(oddIndices) == k:
                leftGap = oddIndices[0] - lastPopped
                ans += leftGap
        return ans
            

# most naive brute force -> n^3
# optimized brute force -> n^2
# sliding window -> n