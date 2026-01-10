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

# O(N) Bucket 
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
    
# Dict + Simulation
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from_stop = collections.defaultdict(int)
        to_stop = collections.defaultdict(int)
        final_stop = 0
        seat = capacity

        for num, f, t in trips:
            from_stop[f] += num
            to_stop[t] += num
            final_stop = max(final_stop, t)

        for stop in range(final_stop + 1):
            if stop in from_stop:
                seat -= from_stop[stop]
            if stop in to_stop:
                seat += to_stop[stop]
            if seat < 0:
                return False

        return True