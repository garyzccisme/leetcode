## 368. Largest Divisible Subset

### Problem Link 
https://leetcode.com/problems/largest-divisible-subset/

### Note
It's easy to find given a number `x` and a divisible set `SET`, if `x % max(SET) = 0`, then `SET.add(x)` can be a
 larger divisible set. 
 
 Create a dict `dp = {num: set(the largest divisible with max = num)}`. Then the problem can be solved in `O(n^2)`.
 
 