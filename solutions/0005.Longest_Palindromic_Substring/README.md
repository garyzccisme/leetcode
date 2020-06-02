## 5. Longest Palindromic Substring

### Problem Link 
https://leetcode.com/problems/longest-palindromic-substring/

### Note
There're two ways to solve this problem: Expanding & DP

Expanding method is easy to understand.

For DP: 

Status Transformation Function
```
dp[i][i] = 1
if s[i] == s[i + 1]: dp[i][i + 1]
if s[i] == s[j]: dp[i][j] = dp[i + 1][j - 1]
```
The status is updated by diagonal.

|   | a | b | c | b | a |
|---|---|---|---|---|---|
| a | 1 | 0 | 0 | 0 | 1 |
| b | 0 | 1 | 0 | 1 | 0 |
| c | 0 | 0 | 1 | 0 | 0 |
| b | 0 | 0 | 0 | 1 | 0 |
| a | 0 | 0 | 0 | 0 | 1 |

