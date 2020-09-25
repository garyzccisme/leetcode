## 179. Largest Number

### Problem Link 
https://leetcode.com/problems/largest-number/

### Note
This problem is a little tricky and I made a mistake with below solution.
```
# This is a wrong solution #

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sort_nums = sorted([str(num) for num in nums], reverse=True)
        return ''.join(sort_nums)
```
At first, the problem is a straight forward sorting puzzle. However, the sorting method above is wrong in some way. 

For example: Given `['30', '3']`, the result should be `'330'`, while the wrong solution returns `303` since 
`sorted(['30', '3']) == ['3', '30']`. 

For this problem, the actual logic is `'3' > '30'` instead of `'3' < '30'`.

Thus we need to define a customized comparator. For more information, please check 
[Leetcode Solution](https://leetcode.com/problems/largest-number/solution/).