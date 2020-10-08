## 61. Rotate List

### Problem Link 
https://leetcode.com/problems/rotate-list/

### Note
The little trick here is to put the `tail` back to `head` so that the list becomes a circle. 
Then we just need to find the cut point and change the circle back to normal list, which is the final result.

For example: given list `[1, 2, 3, 4, 5]` and `k=2`, 
- put list tail back to head, we get an unlimited list `[..., 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...]` and origin list length = 5.
- find correct cut point, 5 - 2 = 3, thus we cut at the third place,  `[..., 1, 2, 3, |4, 5, 1, 2, 3,| 4, 5, ...]`. 
The circle list becomes back to normal list: `[4, 5, 1, 2, 3]`.