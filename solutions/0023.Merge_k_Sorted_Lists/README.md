## 23. Merge k Sorted Lists

### Problem Link 
https://leetcode.com/problems/merge-k-sorted-lists/

### Note
Very Similar with [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/). 

- Merge them one by one could work -> `O(k N)`.
- Use `Heap` can easily figure out the problem. -> `O(N log(N))`
- Also we can think of `Divede and Conquer`-> `O(N log(k))`. 
![alt text](https://leetcode.com/problems/merge-k-sorted-lists/Figures/23/23_divide_and_conquer_new.png)