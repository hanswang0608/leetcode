class Solution:

    def __init__(self, w: List[int]):
        self.prefixProbability = []
        totalSum = sum(w)
        curSum = 0
        for weight in w:
            curSum += weight
            self.prefixProbability.append(curSum / totalSum)

    def pickIndex(self) -> int:
        targetProbability = random.random()
        # return bisect.bisect_right(self.prefixProbability, targetProbability)
        lower, upper = 0, len(self.prefixProbability)-1
        ans = None
        while lower <= upper:
            m = (lower + upper) // 2
            if targetProbability <= self.prefixProbability[m]:
                ans = m
                upper = m - 1
            else:
                lower = m + 1
        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# construct a new array where elements correspond to indices of w and the frequencies of indices match the weight,
# then call a random range function

# use a prefix probability array and binary search for the correct index

# [1,3]
# [1,4]
# [0.25,1]