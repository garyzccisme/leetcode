## 33. Search in Rotated Sorted Array

### Problem Link 
https://leetcode.com/problems/search-in-rotated-sorted-array/

### Note
Although the list is not sorted, but it just get rotated, we can still use `Binary Search` here.

If a sorted array is shifted, if you take the middle, **always one side will be sorted**. Take the recursion according
 to that rule.

Here are the detailed breakdowns of the algorithm:
- Initiate the pointer start to `0`, and the pointer end to `n - 1`.
- Perform standard binary search. While `head` < `tail`:
    - Take an index in the middle `mid` as a pivot.
    - If `nums[mid] == target`, the job is done, return `mid`.
    - Now there could be two situations:
        - Pivot element is larger than the first element in the array, i.e. the subarray from the first element to the 
        pivot is non-rotated, as shown in the following graph.
        ![alt text](https://leetcode.com/problems/search-in-rotated-sorted-array/Figures/33/33_small_mid.png)
        ```  
        - If the target is located in the non-rotated subarray: go left
        - Otherwise: go right
        ```
      - Pivot element is smaller than the first element of the array, i.e. the rotation index is somewhere between 0 
      and mid. It implies that the sub-array from the pivot element to the last one is non-rotated, 
      as shown in the following graph.
      ![alt text](https://leetcode.com/problems/search-in-rotated-sorted-array/Figures/33/33_big_mid.png)
      ```
        - If the target is located in the non-rotated subarray: go right
        - Otherwise: go left
      ```
- We're here because the target is not found. Return -1.