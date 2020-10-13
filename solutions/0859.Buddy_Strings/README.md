## 859. Buddy Strings

### Problem Link 
https://leetcode.com/problems/buddy-strings/

### Note
The key of this problem is to find in what conditions, the result is True.

- `len(A) == len(B)`.
- The difference position length is either 2 or 0.
    - If length is 2, do swap for `A` and then `A == B`.
    - If length is 0, `A == B`, then there must be duplicated letters.
    
After figure out this, the problem can be easily solved by `O(N)` solution.