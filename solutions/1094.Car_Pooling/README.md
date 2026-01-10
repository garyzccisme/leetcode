## 1094. Car Pooling

### Problem Link 
https://leetcode.com/problems/car-pooling/

### Problem Description
Given a list of trips, where each trip is represented as `[num_passengers, start_location, end_location]`, and an integer `capacity` representing the maximum number of passengers the vehicle can hold, determine if it is possible to pick up and drop off all passengers for all the trips without exceeding the vehicle's capacity at any point.

### Solution Approaches

#### 1. Dict + Sorting
- Use two dictionaries to record the number of passengers getting on and off at each location.
- Collect all unique locations and sort them.
- Traverse the sorted locations, updating the current number of passengers.
- If at any point the number exceeds `capacity`, return `False`.
- **Time Complexity:** `O(NlogN)` due to sorting.

#### 2. Heap (Priority Queue)
- Treat each pickup and drop-off as an event and push them into a min-heap by location.
- Pop events in order, updating the current passenger count.
- If the count exceeds `capacity`, return `False`.
- **Time Complexity:** `O(NlogN)` due to heap operations.

#### 3. Bucket (Difference Array / Prefix Sum)
- Since locations are in a known range (0~1000), use an array to record passenger changes at each location.
- For each trip, increment at `start_location` and decrement at `end_location`.
- Traverse the array, maintaining the current passenger count.
- If the count exceeds `capacity`, return `False`.
- **Time Complexity:** `O(N + M)`, where `M` is the range of locations (at most 1001).

#### 4. Dict + Simulation
- Use dictionaries to record the number of passengers getting on and off at each location.
- Find the maximum end location.
- Simulate each stop from 0 to the maximum, updating the seat count.
- If the seat count drops below 0, return `False`.
- **Time Complexity:** `O(M)`, where `M` is the maximum location value.

### Summary
- If location range is small and dense, use the bucket/difference array method for best performance.
- If locations are sparse or not continuous, dictionary-based methods are more space-efficient.
- All methods are based on the idea of tracking passenger changes at each location and checking capacity constraints.
