from collections import defaultdict
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = defaultdict(int)
        for bill in bills:
            change = bill - 5
            register[bill] += 1
            if change == 15:
                if register[10] > 0 and register[5] > 0:
                    register[10] -= 1
                    register[5] -= 1
                elif register[5] >= 3:
                    register[5] -= 3
                else:
                    return False
            elif change == 5:
                if register[5] > 0:
                    register[5] -= 1
                else:
                    return False
        return True

# O(n) -> iterate through and calculate if each customer can get their change