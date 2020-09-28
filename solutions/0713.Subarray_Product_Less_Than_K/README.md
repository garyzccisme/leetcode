## 713. Subarray Product Less Than K

### Problem Link 
https://leetcode.com/problems/subarray-product-less-than-k/

### Note
This problem is a clearly `Two Pointers` & `Sliding Window` problem and should be solved in `O(N)`.

We just need to use a variable `window` to record the product of subarray `nums[left, right + 1]`.
- If `window < k`, the we can count all combinations in subarray into result.
- If `window >= k`, we need to move `right` to left until `window < k`.
- For each loop step, `ans += right - left + 1`.

Example: For given `nums=[1, 2, 3, 4, 5], k=20`, the whole process can be break down as below.

```
left = 0, right = 0, subarray = [1], ans = ans + right - left + 1 = 1
left = 0, right = 1, subarray = [1, 2], ans = ans + right - left + 1 = 3 
left = 0, right = 2, subarray = [1, 2, 3], ans = ans + right - left + 1 = 6
left = 2, right = 3, subarray = [3, 4], ans = ans + right - left + 1 = 8
left = 4, right = 4, subarray = [5], ans = ans + right - left + 1 = 9
```