class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)
        while numsSet:
            start = numsSet.pop()
            i = 1
            while start+i in numsSet:
                numsSet.remove(start+i)
                i+=1
            j = 1
            while start-j in numsSet:
                numsSet.remove(start-j)
                j+=1
            longest = max(longest, i+j-1)

        return longest
            