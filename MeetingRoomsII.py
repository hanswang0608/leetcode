class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        numRoomsNeeded = 0
        for roomStart, roomEnd in intervals:
            if rooms and rooms[0] <= roomStart:
                heapq.heappop(rooms)
            heapq.heappush(rooms, roomEnd)
            numRoomsNeeded = max(numRoomsNeeded, len(rooms))
        return numRoomsNeeded