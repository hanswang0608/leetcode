from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        left = 0
        ans = 0
        for right, fruit in enumerate(fruits):
            basket[fruit] += 1
            while len(basket) > 2 and left < right:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        
# brute force O(n^2) -> try every index as a start pos and iterate
# sliding window O(n) -> sliding window to find longest subarray with at most 2 unique ints

# len of fruits?
# values of fruits?