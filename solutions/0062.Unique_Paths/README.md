## 62. Unique Paths

### Problem Link 
https://leetcode.com/problems/unique-paths/

### Note
This is a very typical `Dynamic Programming` problem. 

The `dp[i][j]` means the number of unique paths at point `(i, j)`.

The state transformation function:
```
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
```

There's a trick: squeeze the `dp` matrix into vector.

Also, this problem is actually a permutation and combination problem thus can be solved in math way: 

- Select m `right` in (m + n) `right & down`.
- The result is `(m + n - 2)! / ((m - 1)! * (n - 1)!)`.
