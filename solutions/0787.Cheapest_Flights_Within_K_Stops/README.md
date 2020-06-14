## 787. Cheapest Flights Within K Stops

### Problem Link 
https://leetcode.com/problems/cheapest-flights-within-k-stops/

### Note
This is a classic `weighted digraph` problem. To find the optimized path, we should first think of `BFS`. Using extra
 `list` or `dict` stores all calculated intermediate values can optimize search.
 
 Besides `BFS with memo`, there's another better `BFS` method: [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). 
 It uses `BFS` like search to solve weighted graph shortest path problem, combined with `Heap` to make sure the search 
 starts with minimum cost path (like greedy algorithm)