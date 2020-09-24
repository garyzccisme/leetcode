## 763. Partition Labels

### Problem Link 
https://leetcode.com/problems/partition-labels/

### Note
This problem is actually a transformation of [Merge Intervals](https://leetcode.com/problems/merge-intervals/). 

- First we need to use a `dict` to gather all sub-intervals.
- By comparing one interval right value with next interval left value, we can determine if to merge both intervals.

The [Leetcode Solution](https://leetcode.com/problems/partition-labels/solution/) is cleaner, but the main idea is
 similar.