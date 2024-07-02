class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        output = []
        for num in nums2:
            if num in count and count[num] > 0:
                count[num] -= 1
                output.append(num)
        return output