# Dict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        get_on = collections.defaultdict(int)
        get_off = collections.defaultdict(int)
        locations = set()

        for num_passengers, start_location, end_location in trips:
            get_on[start_location] += num_passengers
            get_off[end_location] += num_passengers

            locations.add(start_location)
            locations.add(end_location)

        num = 0
        for loc in sorted(locations):
            num += get_on[loc]
            num -= get_off[loc]
            if num > capacity:
                return False
        return True

# Heap
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        travel = []

        for num_passengers, start_location, end_location in trips:
            heapq.heappush(travel, (start_location, num_passengers))
            heapq.heappush(travel, (end_location, -num_passengers))

        cur = 0
        while travel:
            _, num = heapq.heappop(travel)
            cur += num
            if cur > capacity:
                return False
        return True

# O(N) Bucket Sort
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True