class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, cur = 1, 2
        for _ in range(n-2):
            prev, cur = cur, prev + cur
        return cur
        
# base cases:
# f(1)=1
# f(2)=2
# f(n)=f(n-1)+f(n-2)