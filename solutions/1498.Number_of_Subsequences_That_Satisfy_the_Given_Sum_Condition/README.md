## 1498. Number of Subsequences That Satisfy the Given Sum Condition

### Problem Link 
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

### Note
The key point of this problem is to do **sort** for `nums`.

Note that although sort while change the order of list, it actually have no effect on final sub-sequence count. We
 don't care if the elements in sub-sequence is in right order.
 
Example: 
 
```
nums = [5, 7, 6, 3], target = 9

In the sroted list [3, 5, 6, 7], valid sub-squences are [3], [3, 5], [3, 5, 6], [3, 6].
Acually, the right order of the sub-squences are [3], [5, 3], [5, 6, 3], [6, 3].
Alought different in order, the results are same.
```

After figure out this, the problem now is to find out all windows in sorted list where `left + right <= target`. We
 can use `Sliding Window` here.