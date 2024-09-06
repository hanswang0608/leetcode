class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
        stack = [cars[0]]
        for pos, spd in cars:
            frontArrivalTime = (target - stack[-1][0]) / stack[-1][1]
            curArrivalTime = (target - pos) / spd
            if curArrivalTime > frontArrivalTime:
                stack.append((pos, spd))
        return len(stack)

# d = vt + p
# t = (d-p)/t

# brute force
#   - sort cars by position in descending order
#   - simulate per timestep (hour)
#   - iterate through cars and update position based on speed, merge with car ahead if catches up and take min of speed
#   - count number of fleets that arrive

# stack
#   - sort
#   - use monotonically decreasing stack
#   - if current car catches up to head of stack, merge it
#   - nlogn sort, iterate from largest pos to smallest, start a stack with largest
#   - compare each car with top of stack
#       - if it catches up to top of stack, merge it (don't add it to stack)
#       - if it doesn't catch up, it forms a new fleet (push it to stack)