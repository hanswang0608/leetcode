class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            val = numbers[l]+numbers[r]
            if val > target:
                r -= 1
            elif val < target:
                l += 1
            else:
                return [l+1, r+1]
        
# search for element in sorted array -> binary search logN
# cannot reuse element
# elements not unique

# iterate through and binary search for the diff -> worst case NlogN?

# two pointer -> l and r, inc l when too small, dec r when too big