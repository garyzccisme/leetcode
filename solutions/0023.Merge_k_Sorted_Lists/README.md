## 23. Merge k Sorted Lists

### Problem Link 
https://leetcode.com/problems/merge-k-sorted-lists/

### Note
Very Similar with [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/). 

`k` is the number of linked lists, `N` is the number of nodes in final linked list.

- Merge them one by one could work -> `O(k N)`.
- Use `Heap` or `Priority Queue` can easily figure out the problem. -> `O(N log(k))`
- Also we can think of `Divede and Conquer`-> `O(N log(k))`. 
![alt text](https://leetcode.com/problems/merge-k-sorted-lists/Figures/23/23_divide_and_conquer_new.png)