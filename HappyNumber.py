class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def calculate(num):
            output = 0
            while num > 0:
                output += (num % 10) ** 2
                num //= 10
            return output

        while True:
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.add(n)
            n = calculate(n)