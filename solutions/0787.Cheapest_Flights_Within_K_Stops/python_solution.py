# BFS with memo
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # Store lowest cost for traveling to city i
        cities = [float('inf')] * n

        # Store flight information
        flight = collections.defaultdict(list)
        for f in flights:
            flight[f[0]].append((f[1], f[2]))

        fly = collections.deque([(src, 0, 0)])
        while fly:
            city, spend, stop = fly.popleft()

            # If next city cost is visited and cost is higher, then skip
            # If mid stops number exceeds K and the next city isn't desination, then skip
            if cities[city] <= spend or (stop > K and city != dst):
                continue

            cities[city] = spend
            for next_city, next_spend in flight[city]:
                fly.append([next_city, spend + next_spend, stop + 1])

        return -1 if cities[dst] == float('inf') else cities[dst]

# BFS with Heap
# Dijkstra's Algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        flight = collections.defaultdict(dict)
        for start, end, cost in flights:
            flight[start][end] = cost

        # (total_cost, stops, city)
        fly = [(0, 0, src)]
        while fly:
            total_cost, stops, city = heapq.heappop(fly)
            if city == dst:
                return total_cost
            if stops > K:
                continue
            for next_city, cost in flight[city].items():
                heapq.heappush(fly, (total_cost + cost, stops + 1, next_city))
        return -1
