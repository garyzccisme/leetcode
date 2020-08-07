## 442. Find All Duplicates in an Array

### Problem Link 
https://leetcode.com/problems/find-all-duplicates-in-an-array/

### Note
If we are not allowed to use additional memory, the only memory we can use is our original list nums. Let us try to put 
all numbers on they own places, by this I mean, we try to up number `k` to place `k - 1`.

Let us iterate through numbers, and change places for pairs of them, if it is needed. After rearrange, the duplicates
 numbers will be in wrong places.

Example: `[4, 3, 2, 7, 8, 2, 3, 1]` -> `[1, 2, 3, 4, 3, 2, 7, 8]`