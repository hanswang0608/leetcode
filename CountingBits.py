class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n % 2
            n >>= 1
        return ans

    def countBits(self, n: int) -> List[int]:
        return [self.hammingWeight(i) for i in range(n+1)]
        
# brute force O(n): for every i <= n, count its number of bits (constant)

# 5 -> 101
# 6 -> 110
# 7 -> 111
# 8 -> 1000
# 9 -> 1001
# 10 -> 1010
# 11 -> 1011
# 12 -> 1100