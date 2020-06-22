## 174. Dungeon Game

### Problem Link 
https://leetcode.com/problems/dungeon-game/

### Note
Very interesting problem. Here're some ideas about the solutions:

- `Dijkstra Algorithm`. Use `Heap` to store `HP` and position and pop out minimum for each time. But the time
 complexity could be `O(M*N*log(M*N))`. -> Time Limit Exceeded
- `DFS` with memorization, `O(M*N)`.
- `DP`, `O(M*N)`.

My first intuition is to solve this by building up the path from beginning. However, this way leads to local optimal. 

Example: 
```
[1 , -3,  3]        Starting from 1(0,0), we try to maximize the history minimal HP.
[0 , -2,  0]        By this way, the local optimal path is [1, 0, -2, 0, -3], min HP = 5.
[-3, -3, -3]        However, the global optimal path is [1, -3, 3, 0, -3], min HP = 3.
``` 
When these two paths reach `0(1, 2)`, according to the strategy, pick path by `max(min(history min HP))`, then the
 correct path got abandoned. 
 
This brings us to an important observation: **we can solve the problem if we build the solution in reverse.**

After final level, the `min HP = 1`, so we can track back before the level. 
- If the final level number `x` is negative (lose HP), then `min HP = 1 - x`.
- If the final level number `x` is positive (gain HP), then `min HP = 1`, since as long as you are alive (with 1 HP
), you can pass this level.
- `before_final_level_min_HP = max(1, 1 - final_level_gain)`.

Now we can easily find out the state transformation function:

`level_min_HP = max(1, min(down_level_min_HP, right_level_min_HP) - level_gain)`.

According to the function, it's not hard to implement the codes.



