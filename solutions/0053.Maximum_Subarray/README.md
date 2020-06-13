## 53. Maximum Subarray

### Problem Link 
https://leetcode.com/problems/maximum-subarray/

### Note
The problem to find sum or maximum or minimum in an entire array or in a fixed-size sliding window could be solved by
 the dynamic programming (DP) approach in linear time.

There are two standard DP approaches suitable for arrays:

Constant space one. Move along the array and modify the array itself.

Linear space one. First move in the direction left->right, then in the direction right->left. Combine the results. 
Here is an example.

Let's use here the first approach since one could modify the array to track the current local maximum sum at this given point.

Next step is to update the global maximum sum, knowing the local one.

![alt text](https://leetcode.com/problems/maximum-subarray/Figures/53/dp.png)