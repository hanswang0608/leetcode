class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if len(customers) == 0:
            return 0

        lastTime = customers[0][0] + customers[0][1]
        curTime = 0
        total = lastTime - customers[0][0]
        for i in range(1, len(customers)):
            if lastTime >= customers[i][0]:
                curTime = lastTime + customers[i][1]
            else:
                curTime = customers[i][0] + customers[i][1]
            total += curTime - customers[i][0]
            lastTime = curTime
        
        return total / len(customers)