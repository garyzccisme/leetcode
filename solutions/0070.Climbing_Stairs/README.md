## 70. Climbing Stairs

### Problem Link 
https://leetcode.com/problems/climbing-stairs/

### Note
This is a very classic `Dynamic Programming` problem. 

Easy to find out the state transformation function: 

`F(N) = F(N - 1) + F(N - 2)`

- For stairs `N - 2`, make 2 steps to reach stairs `N`
- For stairs `N - 1`, make 1 step to reach stairs `N`
