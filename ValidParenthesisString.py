class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin+1, leftMax+1
            elif c == ")":
                leftMin, leftMax = leftMin-1, leftMax-1
            elif c == "*":
                leftMin, leftMax = leftMin-1, leftMax+1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

# brute force ish O(n*3^m) -> generate every possible string with * (3^m), then check if any of them is valid (n)
# greedy

# (*(*)
# (*)(()