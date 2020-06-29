## 332. Reconstruct Itinerary

### Problem Link 
https://leetcode.com/problems/reconstruct-itinerary/

### Note
Overall, we could consider this problem as a graph traversal problem, where an airport can be viewed as a *vertex* in 
graph and flight between airports as an *edge* in graph. Note that there could be multiple cycles in the graph.
![alt text](https://leetcode.com/problems/reconstruct-itinerary/Figures/332/332_graph.png)

#### 1. Greedy DFS 
Greedy Search for travel path, if reaches end point:
1. If path length is equal to `tickets` length, then finish.
2. If not, means choose wrong direction at last crossing point, backtrack and try another one. 
3. Recursion step 2 search until reaches step 1.

#### 2. Greedy DFS with Stack
This is an optimization of the first approach.
1. Greedy Travel to get a main path, probably miss couple of points.
2. Backtrack all crossing points(departure with multiple arrive), from which we choose the smallest arrive thus miss
 others. We use `stack` here so that the last crossing point pop out first (LIFO).
3. Recurse greedy travel beginning at crossing site.
4. Insert the missing travel cycle path into main path.

#### 3. Eulerian Path
In our problem, we are asked to construct an itinerary that uses all the flights (edges), starting from the airport of 
"JFK". As one can see, the problem is actually a variant of [Eulerian path](https://en.wikipedia.org/wiki/Eulerian_path), 
with a fixed starting point.

- The Algorithm is also `DFS` with greedy strategy. 
- The difference is it's actually `postorder DFS`. That is to do append **after** recursion, thus the points are
 added reversely. Unlike usual `preorder DFS`.
- Need to do extra reverse in the end.
    
