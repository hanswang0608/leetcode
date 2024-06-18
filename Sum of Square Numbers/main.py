class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        while (a <= c and b >= 0):
            val = a**2 + b**2
            if (val < c):
                a += 1
            elif (val > c):
                b -= 1
            else:
                return True
        return False