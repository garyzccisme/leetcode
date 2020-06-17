## 518. Coin Change 2

### Problem Link 
https://leetcode.com/problems/coin-change-2/

### Note
This is a classical dynamic programming problem.

Think of 2D DP matrix. 

- Start from amount = 0 to amount = amount in x axis.
- Start from using only one coin, add one type of coin for each time in y axis.

Status Transformation Function:

`N(amount=x, coin=[a, b]) = N(amount=x, coin=[a]) + N(amount=x - b, coin=[a, b])`

| coin  | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1, 2 | 1 | 1 | 2 | 2 | 3 | 3 | 
| 1, 2, 5 | 1 | 1 | 2 | 2 | 3 | 4 |
