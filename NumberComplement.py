class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        i = 0
        while num > 0:
            if not (num%2):
                ans ^= 1 << i
            num >>= 1
            i += 1
        return ans