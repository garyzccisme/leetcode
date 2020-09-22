## 169. Majority Element

### Problem Link 
https://leetcode.com/problems/majority-element/

### Note
This problem can be solve in many different ways. 
- [Solution Summary](https://leetcode.com/problems/majority-element/solution/)

Here we only discuss the optimal one, **Boyer-Moore Voting Algorithm**.

- Time complexity : `O(N)`
- Space complexity : `O(1)`

Since the majority number is more than half, if we count majority number as +1 and other numbers as -1, then the
 final sum is obviously >0. 

The main idea of the algorithm is to define two variables `candicate` & `count`. 

When doing for loop of the list:
- if current number is same with `candidate`, then `count += 1`. (The `candidate` has one more vote)
- if current number is different with `candidate`, then `count -= 1`. (The `candidate` has one less vote)
- if `count == 0`, then assign current number as new `candidate`. (The previous `candidate` has no vote, so let's
 vote for a new one) 