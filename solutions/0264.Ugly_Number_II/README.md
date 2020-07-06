## 264. Ugly Number II

### Problem Link 
https://leetcode.com/problems/ugly-number-ii/

### Note
To determine if a number is ugly, need to iteratively divided with 2, 3, 5 until can't exact division, if the left
 number is 1 then ugly, else not. This problem also can use such way to find n-th ugly one by one but it's very
  inefficient.
  
Thus we need to think another way: **An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly
 number.**
 
Thus the problem is actually a `three pointers DP` problem.

- In the ugly number sequence, the next ugly number is the minimum of:
    - previous ugly number `U1 * 2`.
    - previous ugly number `U2 * 3`.
    - previous ugly number `U3 * 5`.
- The index of previous ugly number of each factor need to be stored.
- When one factor is selected for next number, the index `+ 1`.
- Note the ugly number could be duplicate.