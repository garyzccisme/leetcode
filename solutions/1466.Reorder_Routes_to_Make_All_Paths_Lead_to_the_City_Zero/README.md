## 1466. Reorder Routes to Make All Paths Lead to the City Zero

### Problem Link 
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

### Analysis
Graph Problem. NOTE in the question `there is only one way to travel between two different cities (this network form
 a tree)`, so there isn't cycle in the graph.
 
 So we can think without direction first, use BFS to travel all the cities. If the direction is inverse, meaning need
  to change it, thus the `count += 1`. 
