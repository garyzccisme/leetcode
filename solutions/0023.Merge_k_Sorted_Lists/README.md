## 23. Merge k Sorted Lists

### Problem Link 
https://leetcode.com/problems/merge-k-sorted-lists/

### Analysis
Very Similar with [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/). 

But here we need to deal with multiple, merge them one by one could work while not efficient `O(k N)`.

Now we can think of `Divede and Conquer`-> `O(N logk)`. 
![alt text](https://leetcode.com/problems/merge-k-sorted-lists/Figures/23/23_divide_and_conquer_new.png)