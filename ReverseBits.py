class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        i = 31

        while n > 0:
            ans |= (n % 2) << i
            n >>= 1
            i -= 1
        
        return ans