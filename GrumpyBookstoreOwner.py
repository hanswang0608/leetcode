class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        for i in range(minutes):
            total += customers[i]

        for i in range(minutes, len(customers)):
            if grumpy[i] != 1:
                total += customers[i]
        
        output = total
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                total += customers[i]
            if grumpy[i-minutes] == 1:
                total -= customers[i-minutes]
            output = max(output, total)

        return output