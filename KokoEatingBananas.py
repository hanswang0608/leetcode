class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:            
        max_speed = max(piles)
        l, r = 1, max_speed
        ans = r
        while l <= r:
            speed = (l+r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/speed)
            if hours <= h:
                r = speed - 1
                ans = speed
            else:
                l = speed + 1
        return ans
        