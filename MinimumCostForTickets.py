class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        tickets = [(1, costs[0]), (7, costs[1]), (30, costs[2])]
        cache = [float('inf')] * 367
        daysSet = set(days)

        for day in range(365, -1, -1):
            if day in daysSet:
                for ticketDuration, ticketPrice in tickets:
                    cachedValue = 0
                    if day + ticketDuration <= 365:
                        cachedValue = cache[day+ticketDuration] if cache[day+ticketDuration] != float('inf') else 0
                    cache[day] = min(cache[day], ticketPrice + cachedValue)
            else:
                cache[day] = cache[day+1]

        return cache[1]