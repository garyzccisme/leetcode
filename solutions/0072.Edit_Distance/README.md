## 72. Edit Distance

### Problem Link 
https://leetcode.com/problems/edit-distance/

### Analysis
This is a classic Dynamic Programming problem. The first thing is to consider about the status matrix and how the status
got transferred.

- When `word1[i] == word[j]`, `dp[i][j] = dp[i - 1][j - 1]`
- When `word1[i] != word[j]`, `dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1`


For word1 = "horse", word2 = "ros". 
We can get the status matrix as below.

|   | # | h | o | r | s | e |
|---|---|---|---|---|---|---|
| # | 0 | 1 | 2 | 3 | 4 | 5 |
| r | 1 | 1 | 2 | 2 | 3 | 4 |
| o | 2 | 2 | 1 | 2 | 3 | 4 | 
| s | 3 | 3 | 2 | 2 | 2 | 3 |


