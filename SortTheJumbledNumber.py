class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # m = defaultdict(list)
        # for num in nums:
        #     m[self.convert(mapping, num)].append(num)
        # output = []
        # for k in sorted(m.keys())
        #     output += m[k]
        # return output
        return sorted(nums, key=lambda num: self.convert(mapping, num))
    
    def convert(self, mapping, num):
        if num == 0:
            return mapping[0]
        output = 0
        digit = 0
        while num > 0:
            output += mapping[num % 10] * 10**digit
            num //= 10
            digit += 1
        return output