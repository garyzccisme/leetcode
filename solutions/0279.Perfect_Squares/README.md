## 279. Perfect Squares

### Problem Link 
https://leetcode.com/problems/count-complete-tree-nodes/

### Note
This problem is quite similar with [322. Coin Change](https://leetcode.com/problems/coin-change/), which is a classic 
backpack problem. Thus the first solution we should think of is `Dynamic Programming`. Also there're some other ways.

#### 1. Dynamic Programming
We can easily write out the state transformation function:

```
numSquares(n) = min(numSquares(n - k) + 1), for k in all square numbers
```
This solution is intuitive. 

#### 2. Greedy DFS
In short, there're 2 ways of doing greedy searching. 

- Greedy for search

The search always starts from the biggest square number. Firstly find a greedy second best solution, then in
 afterward searching, if the count exceeds current "best solution", then break and prune.

- Greedy for count

The search starts from min count (1) to see if it's possible to combine by 1 count, then +1 for each step until find. 

#### 3. Math
The problem can be solved with the mathematical theorems that have been proposed and proved over time, 
[Lagrange's four-square theorem](https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem).

More information can be found at other [explanation](https://leetcode.com/problems/perfect-squares/discuss/707526/Python-Fastest-O(sqrt(n))-solution-with-math-explanied).

