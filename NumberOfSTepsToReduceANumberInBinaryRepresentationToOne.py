class Solution:
    def numSteps(self, s):
        return len(s) + s.rstrip('0').count('0') + 2 * (s.count('1') != 1) - 1