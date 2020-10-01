## 41. First Missing Positive

### Problem Link 
https://leetcode.com/problems/first-missing-positive/

### Note
This problem is marked as **Hard** level. Using `Sort` or `Hash Map` is very easy and straight forward. However, the
 problem asks for `O(N)` time and `O(1)` space.
 
Notice that the first positive number will be in the range of `1, 2, 3, ..., len(nums), len(nums) + 1` by order. So
 here we can rearange the `nums` list by putting each number at its place.
 
For `nums[i]`, we swap it with `nums[nums[i] - 1]` so that `nums[i]` can be at it's position. 
Thus we can design an iteration to keep swapping `nums[i]` until it's already in its place.

Example: for given `nums=[-1, 3, 1, 4, 2, 6]`, the break down of iteration is as follows.
```
nums = [-1, 3, 1, 4, 2, 6], i = 0, since -1 not in range(1, len(nums) + 1), i += 1
nums = [-1, 1, 3, 4, 2 ,6], i = 1, since 3(nums[1]) not in its place, swap with 1(nums[2])
nums = [1, -1, 3, 4, 2, 6], i = 1, since 1(nums[1]) not in its place, swap with -1(nums[0]), i += 1
nums = [1, -1, 3, 4, 2, 6], i = 2, 3(nums[2]) is in its place, i += 1
nums = [1, -1, 3, 4, 2, 6], i = 3, 4(nums[3]) is in its place, i += 1
nums = [1, 2, 3, 4, -1, 6], i = 4, 2(nums[4]) not in its place, swap with -1(nums[1]), i += 1
nums = [1, 2, 3, 4 ,-1, 6], i = 5, 6(nums[5]) is in its place, finish
``` 
Finally we just need to do a simple iteration to find out the missing number which is the first missing positive.

More thinking:
This solution is similar with [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/).
As the range of targets is given, we can think of swapping trick to achieve `O(1)` space complexity.
 


