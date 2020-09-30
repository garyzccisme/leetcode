## 139. Word Break

### Problem Link 
https://leetcode.com/problems/word-break/

### Note
This problem is a classical `DP` problem. Here I list two solutions.

#### 1. Memoization DFS
We can use a recursive function to implement `DFS` process. 

Note here we must define a memoization `dict` to avoid duplicated calculation. Otherwise the solution will meet `Time
 Limit Exceeded` error.
 
#### 2. Dynamic Programming
In the `dp` list, `dp[i]` stands for the work break result of `s[:i]`.

If `dp[i]` is True:
- There must be at least one word in `wordDict` that meets the end of `s[:i]`.
- For the matched word, backtrack `dp[i - len(word)]`. If True, then `dp[i] = True`. 