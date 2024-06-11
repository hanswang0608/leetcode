class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        output = []
        for num in arr2:
            for _ in range(count[num]):
                output.append(num)
            count.pop(num)
        
        remainder = []
        for num in count:
            for _ in range(count[num]):
                remainder.append(num)
        
        remainder.sort()
        output += remainder
        return output